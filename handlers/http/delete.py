import json
from common.aws import books_table
from common.broadcast import broadcast

def handler(event, context):
    book_id = event["pathParameters"]["id"]

    books_table.delete_item(Key={"bookId": book_id})

    broadcast({
        "type": "bookDeleted",
        "bookId": book_id
    })

    return {
        "statusCode": 204,
        "body": ""
    }
