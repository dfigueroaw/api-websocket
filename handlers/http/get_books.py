from common.aws import books_table
from common.response import response

def handler(event, context):
    res = books_table.scan()
    books = res.get("Items", [])

    return response(200, books)
