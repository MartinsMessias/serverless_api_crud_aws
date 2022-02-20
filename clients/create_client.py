import json
import uuid
import boto3

conn_ddb = boto3.resource('dynamodb').Table('clients')

def create_client(event, context):
    try:
        body = json.loads(event["body"])
        client = {
            "id":str(uuid.uuid4()),
            "name": body["name"]
        }
        
        conn_ddb.put_item(Item=client)
        response = {"statusCode": 200, "body": json.dumps({"client": client})}
        return response
    except Exception as e:
        response = {"statusCode": 400, "body": json.dumps({"error": "Bad request"+str(e)})}
        return response
