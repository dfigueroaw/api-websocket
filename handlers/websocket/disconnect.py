from common.aws import connections_table

def handler(event, context):
    connection_id = event["requestContext"]["connectionId"]

    connections_table.delete_item(
        Key={"connectionId": connection_id}
    )

    return {"statusCode": 200}
