"""
PROGRAM NAME: rds_start_db_instance.py
PROGRAM POURPOSE: to demonstrate the starting of a db instance
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
rds = boto3.client('rds', region_name='us-west-2')

def start_db_instance(instance_id):
    response = rds.start_db_instance(
        DBInstanceIdentifier=instance_id
    )
    return response


