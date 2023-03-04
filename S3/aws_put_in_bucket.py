"""
PROGRAM NAME: aws_put_in_bucket.py
PROGRAM POURPOSE: demonstrates a simple bucket insertion using the boto3 api (if your credentials are configured, it should work for you... aws configure)
DATE WRITTEN: 1/5/22
PROGRAMMER: Coulter C. Stutz
"""
import logging

import boto3
import botocore.credentials
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def upload_files(bucketname, filename):

    try:
        response = s3.upload_file(filename, bucketname)
        return True
    except ClientError:
        return False


print(upload_files('coulterprivatecloud', 'test.txt'))
