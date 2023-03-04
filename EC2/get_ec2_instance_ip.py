"""
PROGRAM NAME: ec2_get_instance_ip.py
PROGRAM PURPOSE: to retrieve an instance ip
DATE WRITTEN: 1/10/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

ec2 = boto3.client('ec2', region_name='us-west-2')
instances = []

ec2.describe_instances()
