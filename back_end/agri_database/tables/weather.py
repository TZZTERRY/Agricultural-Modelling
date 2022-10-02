import boto3

"""
this table stores the data of historical weather values
"""


def create_weather_table(dynamodb=None):
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


if __name__ == '__main__':
    book_table = create_weather_table()
    # print("Tablestatus:", book_table.table_status)

    # TODO: Add all temperature with different regions and years
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Weather")
    table.put_item(
        Item={
            'title': 'QLD',
            'year': 1999,
            "value": '34'
        }
    )

    print(table.get_item(
        Key={
            'title': '02',
            'year': 1999
        }
    ))
