import boto3
from botocore.config import Config
import os

os.environ['AWS_PROFILE'] = 'hungtran'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

dynamodb = boto3.client('dynamodb', region_name='us-east-1')
print("[INFO:] Connecting to cloud")

table = dynamodb.create_table(
    TableName='DanceEvents',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)


