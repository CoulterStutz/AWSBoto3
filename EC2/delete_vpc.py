"""
PROGRAM NAME: delete_vpc.py
PROGRAM PURPOSE: to delete a vpc
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
import botocore

ec2 = boto3.client('ec2', region_name='us-west-2')
def delete_vpcs(*args):
    responses = ''
    for x in args:
        try:
            response = ec2.delete_vpc(
                VpcId=x,
            )
            print(response)
        except botocore.exceptions.ClientError:
            print(f'VPC {x}: does not exist, moving on')
if __name__ == "__main__":
    print(delete_vpcs(''))
