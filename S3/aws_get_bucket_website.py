"""
PROGRAM NAME: aws_get_bucket_websote.py
PROGRAM POURPOSE: demonstrates the getting of a bucket website
DATE WRITTEN: 1/26/22
PROGRAMMER: Coulter C. Stutz
"""
import boto3
s3 = boto3.client('s3')

def get_bucket_website(bucket_name):
    response = s3.get_bucket_website(
        Bucket=bucket_name,
    )
    return response


