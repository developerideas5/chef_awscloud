import boto3 
from botocore.exceptions import ClientError

print('Loading Function')

SENDER = "shrutikulkarni0005@gmail.com"
RECIPIENT= "shrutikulkarni0005@gmail.com"
SUBJECT = "New User Registration"
BODY_TEXT = "Congratulations! A new user has signed up on the website!"

AWS_REGION = "us-east-1"
CHARSET = "UTF-8"

def lambda_handler(event, context):

	client = boto3.client("ses",region_name=AWS_REGION)

	try:
		response = client.send_email(
			Destination={'ToAddress': [
			RECIPIENT,],
			},
			Message={
			'Body': {
			'Text': {
			'Charset': CHARSET,
			'Data': BODY_TEXT,
			},
			},
			'Subject': {
			'Charset': CHARSET,
			'Data': SUBJECT,
			},
			},
			Source=SENDER)

		#ErrorHandling
	except ClientError as e:
		print(e.response['Error']['Message'])
	else:
		print("Email Sent Successfuly! MessageID: "),
		print(reposnse['MessageId'])





