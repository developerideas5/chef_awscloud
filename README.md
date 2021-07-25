# chef_awscloud

1.email_lamda_function.py

Send an email on additional of items in DynamoDB Table using lambda Function and SES 
SDK 
I. Add & Verify an email address to be used as recipient in SES service.
2. Create an IAM role for Lambda giving it SES and DynamoDB full access.
3. Create a Python function in Lambda using the created role in step 2 and the shared script.
4. Create Table in dynamoDB using the name "users" and primary key as "userid". 
5. Add as trigger in lambda function created in step3.
6. Enable Stream property to manage all input and output stream in the table 
7. Deploy EC2 instance(Ubuntu, t2.micro, SSH port open) 
8. Install Python, pip and packages 
9. Create directory in instance using: sudo mkdir 
10. Update default region using: echo -e > .qws/config 
11. Create and execute python script. 

#dynamo.py

import bot03 
if '—main_ 
Item={ 
'userid': 101, 
'name' : "Jane Doe", 
'city' : "NYC", 
'county' : "USA" 
