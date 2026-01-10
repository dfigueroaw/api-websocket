import os
import boto3

BOOKS_TABLE = os.environ["BOOKS_TABLE"]
CONNECTIONS_TABLE = os.environ["CONNECTIONS_TABLE"]
WS_ENDPOINT = os.environ["WS_ENDPOINT"]

dynamodb = boto3.resource("dynamodb")
books_table = dynamodb.Table(BOOKS_TABLE)
connections_table = dynamodb.Table(CONNECTIONS_TABLE)

apigw = boto3.client(
    "apigatewaymanagementapi",
    endpoint_url=WS_ENDPOINT
)
