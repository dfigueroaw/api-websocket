import json
from common.aws import books_table
from common.broadcast import broadcast
from common.response import response

def handler(event, context):
    body = json.loads(event.get("body", "{}"))

    book_id = body.get("bookId")
    title = body.get("title")

    if not book_id or not title:
        return response(400, "bookId and title are required")

    book = {
        "bookId": book_id,
        "title": title,
        "available": True,
        "borrowedBy": None
    }

    books_table.put_item(Item=book)

    broadcast({
        "type": "bookCreated",
        "book": book
    })

    return response(201, book)
