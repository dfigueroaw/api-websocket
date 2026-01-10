import os
from common.aws import connections_table

def handler(event, context):
    connection_id = event["requestContext"]["connectionId"]

    connections_table.put_item(
        Item={"connectionId": connection_id}
    )

    return {"statusCode": 200}
