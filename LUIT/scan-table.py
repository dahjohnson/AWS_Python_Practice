import boto3
import json

client = boto3.client('dynamodb')

response = client.scan(
    TableName='mcu-characters')
    
for i in response['Items']:
    print(json.dumps(i, indent=2))