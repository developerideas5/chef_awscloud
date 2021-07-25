import boto3
if __name__='__main__':
    dynamodb = boto3.resource('dynamodb')
    table=dynamodb.Table('users')
    response=table.put_item(
        Item={
        'userid': 101,
        'name' : "Jane Doe",
        'city' : "NYC",
        'country' : "USA"
        }
    )
    print("Item Entry Successfully!")
