"""
PROGRAM NAME: delete_volume.py
PROGRAM PURPOSE: to delete ec2 volumes
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
import botocore

ec2 = boto3.client('ec2', region_name='us-west-2')

def delete_volumes(*args):
    for x in args:
        try:
            response = ec2.delete_volume(
                VolumeId=x,
                DryRun=False
            )
            print(response)

        except botocore.exceptions.ClientError:
            print(f'Volume {x}: does not exist, moving on')

if __name__ == "__main__":
    delete_volumes()
