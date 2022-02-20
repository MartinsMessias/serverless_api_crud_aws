import json
import boto3

conn_ddb = boto3.resource('dynamodb').Table('clients')


def update_client(event, context):
    try:
        id = event["pathParameters"]["id"]
        body = json.loads(event["body"])
        client = {
            "id": id,
            "name": body["name"]
        }
        conn_ddb.put_item(Item=client)
        response = {"statusCode": 200, "body": json.dumps({"client": client})}
        return response
    except Exception as e:
        response = {"statusCode": 400, "body": json.dumps({"error": "Bad request"+str(e)})}
        return response