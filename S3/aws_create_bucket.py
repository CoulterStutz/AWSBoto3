"""
PROGRAM NAME: aws_put_in_bucket.py
PROGRAM POURPOSE: demonstrates a simple bucket insertion using the boto3 api (if your credentials are configured, it should work for you... aws configure)
DATE WRITTEN: 1/5/22
PROGRAMMER: Coulter C. Stutz
"""

import boto3, botocore

ACL_settings = ['private', 'public-read', 'public-read-write', 'authenticated-read']
LocationConstraints = ['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1',
                       'ap-southeast-1', 'ap-southeast-2', 'ap-southeast-3', 'ca-central-1', 'cn-north-1',
                       'cn-northwest-1', 'EU', 'eu-central-1', 'eu-north-1', 'eu-south-1', 'eu-west-1', 'eu-west-2',
                       'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1',
                       'us-west-1', 'us-west-2']

s3 = boto3.client('s3')


def create_bucket(bucketname):

    response = s3.create_bucket(
        Bucket=bucketname,
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )

    return response


print(create_bucket('awsrepositorypython'))
