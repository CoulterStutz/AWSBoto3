"""
PROGRAM NAME: aws_delete_objects.py
PROGRAM POURPOSE: demonstrates a simple object deletion
DATE WRITTEN: 1/26/22
PROGRAMMER: Coulter C. Stutz
"""
import boto3
s3 = boto3.client('s3')

def delete_objects(bucket_name, key, bypass_retention:bool):
    response = s3.delete_object(
        Bucket=bucket_name,
        Key=key,
        BypassGovernanceRetention=bypass_retention,
    )
    return response
