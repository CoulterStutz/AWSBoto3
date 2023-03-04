"""
PROGRAM NAME: rds_stop_db_instance.
PROGRAM POURPOSE: to demonstrate the stopping of a rds instance
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
rds = boto3.client('rds', region_name='us-west-2')

def stop_rds_instance(instance_id):
    response = rds.stop_db_instance(
        DBInstanceIdentifier=instance_id,
    )

    return response

