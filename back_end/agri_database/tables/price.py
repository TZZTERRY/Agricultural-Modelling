import boto3

"""
this table stores the data of price
"""


def create_price_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName='Price',
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
    book_table = create_price_table()
    # print("Tablestatus:", book_table.table_status)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Price")
    table.put_item(
        Item={
            'title': '02',
            'year': 2024,
            "value": '3420'
        }
    )
    print(table.get_item(
        Key={
            'title': '02',
            'year': 2002
        }
    ))
