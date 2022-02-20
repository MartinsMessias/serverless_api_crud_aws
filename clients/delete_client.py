import json
import boto3

conn_ddb = boto3.resource('dynamodb').Table('clients')


def delete_client(event, context):
    try:
        id = event["pathParameters"]["id"]
        conn_ddb.delete_item(Key={"id": id})
        response = {"statusCode": 200, "body": json.dumps({"message": "Client deleted"})}
        return response
    except Exception as e:
        response = {"statusCode": 404, "body": json.dumps({"error": "Client not found"+str(e)})}
        return response