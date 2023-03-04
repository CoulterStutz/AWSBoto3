"""
PROGRAM NAME: terminate_ec2_instances.py
PROGRAM PURPOSE: to terminate ec2 instances
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3, botocore

ec2 = boto3.client('ec2', region_name='us-west-2')

def terminate_ec2_instances(*args):
    """Instance IDs to Terminate"""

    for x in args:
        try:
            response = ec2.terminate_instances(
                InstanceIds=[
                    x,
                ],
                DryRun=True
            )
            print(response)
        except botocore.exceptions.ClientError:
            print(f'EC2 Instance {x}: cannot be found!')

if __name__ == "__main__":
    print(terminate_ec2_instances("i-0e16977d79fe96403", "i-0e7475acf4b77496e"))

