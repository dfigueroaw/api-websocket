import json
from common.aws import books_table

def handler(event, context):
    response = books_table.scan()
    books = response.get("Items", [])

    return {
        "statusCode": 200,
        "body": json.dumps(books)
    }
