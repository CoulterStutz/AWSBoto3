"""
PROGRAM NAME: start_ec2_instances.py
PROGRAM PURPOSE: to start ec2 instances
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3, botocore

ec2 = boto3.client('ec2', region_name='us-west-2')

def start_ec2_instances(*args):
    """Instance IDs to Start"""

    for x in args:
        try:
            response = ec2.start_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=True
            )
            print(response)
        except botocore.exceptions.ClientError:
            print(f'EC2 Instance {x}: cannot be found!')

if __name__ == "__main__":
    print(start_ec2_instances(""))
