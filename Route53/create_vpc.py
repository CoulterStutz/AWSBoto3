"""RIPPED FROM EC2 LIBRARY
PROGRAM NAME: create_vpc.py
PROGRAM PURPOSE: to create a vpc
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""
import json

import boto3

ec2 = boto3.client('ec2', region_name='us-west-2')

def create_vpc(Name, CidrBlock, aws_auto_ipv6:bool, instance_tendency, Ipv6_Pool=0, Ipv6_CidrBlock=0):

    if aws_auto_ipv6:
            response = ec2.create_vpc(
                CidrBlock=CidrBlock,
                AmazonProvidedIpv6CidrBlock=True,
                DryRun=False,
                InstanceTenancy=instance_tendency,
                TagSpecifications=[
                        {
                            'ResourceType': 'vpc',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value': Name
                                },
                            ]
                        },
                ]
            )
            return response
    else:
        try:
            assert len(Ipv6_Pool) != 0
        except AssertionError:
            return 'IPv6_pool cannot be empty if aws_auto_ipv6 is set to true'

        try:
            assert len(Ipv6_CidrBlock) != 0
        except AssertionError:
            return 'IPv6_CidrBlock cannot be empty if aws_auto_ipv6 is set to true'

        response = ec2.create_vpc(
            CidrBlock=CidrBlock,
            AmazonProvidedIpv6CidrBlock=False,
            Ipv6Pool=Ipv6_Pool,
            Ipv6CidrBlock=Ipv6_CidrBlock,
            DryRun=False,
            InstanceTenancy=instance_tendency,
            TagSpecifications=[
                    {
                        'ResourceType': 'vpc',
                        'Tags': [
                            {
                                'Key': 'Name',
                                'Value': Name
                            },
                        ]
                    },
            ]
        )

if __name__ == "__main__":
    print(create_vpc('MyVPC', '192.168.1.1/24', True, 'default'))
