import json
from common.aws import books_table
from common.broadcast import broadcast

def handler(event, context):
    book_id = event["pathParameters"]["id"]

    response = books_table.get_item(Key={"bookId": book_id})
    if "Item" not in response:
        return {
            "statusCode": 404,
            "body": "Book not found"
        }

    book = response["Item"]
    if book.get("available", True):
        return {
            "statusCode": 409,
            "body": "Book is not currently borrowed"
        }
    
    book["available"] = True
    book["borrowedBy"] = None

    books_table.put_item(Item=book)

    broadcast({
        "type": "bookReturned",
        "book": book
    })

    return {
        "statusCode": 200,
        "body": json.dumps(book)
    }
