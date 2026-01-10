import json
from common.aws import apigw, connections_table

def broadcast(payload: dict):
    connections = connections_table.scan()["Items"]
    for c in connections:
        try:
            apigw.post_to_connection(
                ConnectionId=c["connectionId"],
                Data=json.dumps(payload)
            )
        except Exception:
            pass
