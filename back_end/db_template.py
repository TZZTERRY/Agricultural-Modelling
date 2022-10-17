import boto3
import time
from agri_csv_reader import read_csv
"""
the template to update remote database
"""
def create_book_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Book',
        KeySchema=[
            {
                'AttributeName': 'title',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'year',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table


def create_weather_table(dynamodb=None):
    """
    Creat the weather table
    :param dynamodb:
    :return:
    """

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Weather',
        KeySchema=[
            {
                'AttributeName': 'region_name',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'year',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'region_name',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table

def create_yield_price_table(dynamodb=None):
    """
    Creat the Yield_Price table
    :param dynamodb:
    :return:
    """

    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Yield_Price',
        KeySchema=[
            {
                'AttributeName': 'region_crop',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'year',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'region_crop',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    return table

def put_crop_item():
    """
    read crop data and put into DB
    :return:
    """


if __name__ == '__main__':
    table = create_yield_price_table()
    time.sleep(0.1)
    print("Tablestatus:", table.table_status)
    exit()

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Book")
    table.put_item(
        Item={
            'title': '02',
            'year': 2022,
            "value": '12345'
        }
    )
    print(table.get_item(
        Key = {
        'title': '02',
        'year': 2022
    }
    ))