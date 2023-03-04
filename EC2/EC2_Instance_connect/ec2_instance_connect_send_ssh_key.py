"""
PROGRAM NAME: ec2_instance_connect_send_ssh_key.py
PROGRAM POURPOSE: demonstrates an ssh key transaction from the cloud
DATE WRITTEN: 1/13/22
PROGRAMMER: Coulter C. Stutz
"""

import boto3

ec2_instance_connect = boto3.client('ec2-instance-connect', region_name='ap-northeast-1')

def send_ssh_public_key(instance_id, instance_os_user, SSH_public_key):
    response = ec2_instance_connect.send_ssh_public_key(
        InstanceId=instance_id,
        InstanceOSUser=instance_os_user,
        SSHPublicKey=SSH_public_key
    )
    return response
