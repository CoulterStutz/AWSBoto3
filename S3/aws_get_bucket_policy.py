"""
PROGRAM NAME: aws_get_bucket_policy.py
PROGRAM POURPOSE: gets a bucket policy
DATE WRITTEN: 1/26/22
PROGRAMMER: Coulter C. Stutz
"""
import boto3
s3 = boto3.client('s3')

def get_bucket_policy(bucket_name):
    response = s3.get_bucket_policy(
        Bucket=bucket_name
    )
    return response


