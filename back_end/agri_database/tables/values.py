import boto3

"""
this table stores the data of  predicting yields 
"""


def create_values_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Values',
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


if __name__ == '__main__':
    book_table = create_values_table()
    # print("Tablestatus:", book_table.table_status)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Values")
    table.put_item(
        Item={
            'title': '02',
            'year': 2023,
            "value": '3420'
        }
    )
    print(table.get_item(
        Key={
            'title': '02',
            'year': 2023
        }
    ))
