import json
import boto3

conn_ddb = boto3.resource('dynamodb').Table('clients')

def get_client(event, context):
    try:
        id = event["pathParameters"]["id"]
        client = conn_ddb.get_item(Key={"id": id})["Item"]
        response = {"statusCode": 200, "body": json.dumps({"client": client})}
        return response
    except Exception as e:
        response = {"statusCode": 404, "body": json.dumps({"error": "Client not found"+str(e)})}
        return response