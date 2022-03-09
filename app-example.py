import logging
import boto3
import json
import pprint
import os
from appexamplefunctions import put_movie
AWS_REGION = 'us-east-2'
AWS_PROFILE = 'localstack'
ENDPOINT_URL = "localhost:4566"

# logger config
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s: %(levelname)s: %(message)s')

boto3.setup_default_session(profile_name=AWS_PROFILE)


if __name__ == '__main__':
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:4566")
    tables = list(dynamodb.tables.all())
    print(tables)
    movie_resp = put_movie("The Big New Movie", 2015,
                           "Nothing happens at all.", 5, dynamodb=dynamodb)
    print("Put movie succeeded:")
    pprint.pprint(movie_resp, sort_dicts=False)