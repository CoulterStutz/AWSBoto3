"""
PROGRAM NAME: stop_ec2_instances.py
PROGRAM PURPOSE: to stop ec2 instances
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3, botocore

ec2 = boto3.client('ec2', region_name='us-west-2')

def stop_ec2_instances(*args):
    """Instance IDs to Stop"""

    for x in args:
        try:
            response = ec2.stop_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=True
            )
            print(response)
        except botocore.exceptions.ClientError:
            print(f'EC2 Instance {x}: cannot be found!')

if __name__ == "__main__":
    print(stop_ec2_instances('i-0a75bbd00f1a609a8'))
