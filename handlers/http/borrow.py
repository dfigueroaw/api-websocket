import json
from common.aws import books_table
from common.broadcast import broadcast
from common.response import response

def handler(event, context):
    book_id = event["pathParameters"]["id"]
    body = json.loads(event.get("body", "{}"))

    borrowed_by = body.get("borrowedBy")
    if not borrowed_by:
        return response(400, "borrowedBy is required")

    res = books_table.get_item(Key={"bookId": book_id})
    if "Item" not in res:
        return response(404, "Book not found")

    book = res["Item"]

    if not book.get("available", True):
        return response(409, "Book is already borrowed")

    book["available"] = False
    book["borrowedBy"] = borrowed_by

    books_table.put_item(Item=book)

    broadcast({
        "type": "bookBorrowed",
        "book": book
    })

    return response(200, book)
