import json
from common.aws import books_table
from common.broadcast import broadcast
from common.response import response

def handler(event, context):
    book_id = event["pathParameters"]["id"]

    response = books_table.get_item(Key={"bookId": book_id})
    if "Item" not in response:
        return response(404, "Book not found")

    book = response["Item"]
    if book.get("available", True):
        return response(409, "Book is not currently borrowed")
    
    book["available"] = True
    book["borrowedBy"] = None

    books_table.put_item(Item=book)

    broadcast({
        "type": "bookReturned",
        "book": book
    })

    return response(200, book)
