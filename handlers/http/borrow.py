import json
from common.aws import books_table
from common.broadcast import broadcast

def handler(event, context):
    book_id = event["pathParameters"]["id"]
    body = json.loads(event.get("body", "{}"))

    borrowed_by = body.get("borrowedBy")
    if not borrowed_by:
        return {
            "statusCode": 400,
            "body": "borrowedBy is required"
        }

    response = books_table.get_item(Key={"bookId": book_id})
    if "Item" not in response:
        return {
            "statusCode": 404,
            "body": "Book not found"
        }

    book = response["Item"]
    if not book.get("available", True):
        return {
            "statusCode": 409,
            "body": "Book is already borrowed"
        }

    book["available"] = False
    book["borrowedBy"] = borrowed_by

    books_table.put_item(Item=book)

    broadcast({
        "type": "bookBorrowed",
        "book": book
    })

    return {
        "statusCode": 200,
        "body": json.dumps(book)
    }
