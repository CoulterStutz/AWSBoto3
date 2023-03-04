"""
PROGRAM NAME: aws_delete_bucket_website.py
PROGRAM POURPOSE: demonstrates a simple website deletion
DATE WRITTEN: 1/26/22
PROGRAMMER: Coulter C. Stutz
"""
import boto3
s3 = boto3.client('s3')

def delete_bucket_website(bucket_name):
    response = s3.delete_bucket_website(
        Bucket=bucket_name,
    )
    return response
