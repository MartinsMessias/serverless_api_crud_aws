import decimal
import json
import boto3

conn_ddb = boto3.resource('dynamodb').Table('clients')

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  #<---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)

def get_clients(event, context):
    try:
        clients = conn_ddb.scan()["Items"]
        response = {"statusCode": 200, "body": json.dumps({"clients": clients}, cls=DecimalEncoder)}
        return response
    except Exception as e:
        response = {"statusCode": 404, "body": json.dumps({"error": "Clients not found."+str(e)})}
        return response