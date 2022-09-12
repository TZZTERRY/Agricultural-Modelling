import boto3
from boto3 import Session
from boto3.dynamodb.conditions import Attr, Key
import json


class DynamoDBService:
    def __int__(self):
        self.AWS_ACCESS_ID = 'AKIAVD5HUV2TNH6TEXHB'
        self.AWS_ACCESS_KEY = 'HWJNbN0/0inKCZcIBBC7MD5JqPpAemQ3KM0zvmjK'

    def get_service(self, table_name):
        client = boto3.client('dynamodb', region_name='us-east-1', aws_access_key_id=self.AWS_ACCESS_ID,
                              aws_secret_access_key=self.AWS_ACCESS_KEY)
        dynamodb = boto3.resource('dynamodb',region_name='us-east-1',aws_access_key_id = self.AWS_ACCESS_ID,
                                  aws_secret_access_key = self.AWS_ACCESS_KEY)

        table_handle = dynamodb.Table(table_name)
        return table_handle

    def operate_table(self, table_name='cropData', name='wheat'):
        table_handle_h5_visit_info = self.get_service(table_name)

        response = table_handle_h5_visit_info.query(keyConditionExpression = Key('name').eq(name))

        print(type(response))
        items = response['Items']
        print(items)
        return json.dumps(items)

