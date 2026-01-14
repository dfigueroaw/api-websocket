import json

def response(status_code: int, body=None):
    raw_body = None

    if body is not None:
        if isinstance(body, str):
            raw_body = body
        else:
            raw_body = json.dumps(body)
    
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*",
        },
        "body": raw_body,
    }
