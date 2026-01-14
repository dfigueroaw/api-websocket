from common.aws import books_table
from common.response import response

def handler(event, context):
    response = books_table.scan()
    books = response.get("Items", [])

    return response(200, books)
