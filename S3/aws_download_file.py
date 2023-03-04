"""
PROGRAM NAME: aws_download_files.py
PROGRAM POURPOSE: demonstrates a file download
DATE WRITTEN: 1/26/22
PROGRAMMER: Coulter C. Stutz
"""
import boto3
s3 = boto3.client('s3')

def download_object(bucket_name, object_name, download_location):
    s3.meta.client.download_file(bucket_name, object_name, download_location)
