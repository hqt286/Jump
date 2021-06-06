import boto3
from botocore.config import Config
from botocore.exceptions import ClientError
from eventservice.dao.BaseDAO import BaseDAO
import os
import uuid
from eventservice.serializer.EventSerializer import EventSerializer

os.environ['AWS_PROFILE'] = 'hungtran'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'

DANCE_EVENTS_TABLE = 'DanceEvents'


class DanceEventDAO(BaseDAO):
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table(DANCE_EVENTS_TABLE)

    @classmethod
    def create(cls, event):
        print(event)
        if event.id is not None:
            return
        event.id = uuid.uuid1().int
        serializer = EventSerializer(event)
        cls.table.put_item(Item=serializer.data)

    @classmethod
    def update(cls, event):
        serializer = EventSerializer(event)
        cls.table.update_item(
            Key={"id": event.id},
            ExpressionAttributeValues={":cb": {'S': event.createdBy}},
            UpdateExpression="SET createdBy = :cb",
            ReturnValues="UPDATED_NEW"
        )

    @classmethod
    def removeById(cls, id):
        # TODO Add safeguard method. This is not completed
        response = cls.table.delete_item(Key={'id': int(id)})
        return response

    @classmethod
    def getById(cls, id):
        try:
            response = cls.table.get_item(Key={'id': int(id)})
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            return response['Item']