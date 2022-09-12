import json
from cropData import crop_Data
from DynamoDBService import DynamoDBService


def lambda_handler(event, context):
    myname = event.get('name', 'wheat')

    dynamodb = DynamoDBService()

    result = dynamodb.operate_table(name=myname)
    return {
        'statusCode': 200,
        'body' : result
    }

def cropData(e):
    print(e)
    return {
        'name': e.name,
        'year': e.year,
        'values': e.values,
        'regionname': e.regionname
    }
