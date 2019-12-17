import boto3
from logic.pkg_test import Logic

l = Logic()

session = boto3.Session(profile_name='access-yes')
access_yes  = session.client('s3')

l.list_buckets(access_yes)