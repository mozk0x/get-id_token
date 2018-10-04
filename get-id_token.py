import json
import urllib.request
from warrant.aws_srp import AWSSRP
import getpass

# init
POOL_ID = 'ap-northeast-1_HNT0fUj4J'
POOL_REGION = 'ap-northeast-1'
CLIENT_ID = '2gri5iuukve302i4ghclh6p5rg'
# set login user_id
USERNAME = input('User ID: ')
# set login password
PASSWORD = getpass.getpass('Password: ')

# get id token
aws = AWSSRP(username=USERNAME, password=PASSWORD, pool_id=POOL_ID, client_id=CLIENT_ID, pool_region=POOL_REGION)
id_token = aws.authenticate_user()['AuthenticationResult']['IdToken']

print(id_token)
