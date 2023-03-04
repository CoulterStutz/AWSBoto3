"""
PROGRAM NAME: create_volume.py
PROGRAM PURPOSE: to delete ec2 volumes
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
import botocore

ec2 = boto3.client('ec2', region_name='us-west-2')

def create_volume(avalibility_zone, encrypted:bool, Size, volumeType, multiAttach: bool, amount_of_volumes):
    for x in range(amount_of_volumes):
        response = ec2.create_volume(
            AvailabilityZone=avalibility_zone,
            Encrypted=encrypted,
            Size=Size,
            VolumeType=volumeType,
            DryRun=False,
            MultiAttachEnabled=multiAttach
        )
        print(response)

if __name__ == "__main__":
    create_volume('us-west-2d', True, 8, 'gp2', False, 1)
