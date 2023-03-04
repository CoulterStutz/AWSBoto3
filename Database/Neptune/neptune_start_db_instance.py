"""
PROGRAM NAME: neptune_start_db_instance.py
PROGRAM PURPOSE: demonstrates the starting of a graphical neptune database
DATE WRITTEN: 1/13/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

neptune = boto3.client('neptune', region_name='us-west-2')

def neptune_start_db_instance(instance_id):
    response = neptune.start_db_instance(
        DBInstanceIdentifier=instance_id
    )
    return response
