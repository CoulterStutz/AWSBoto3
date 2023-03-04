"""
PROGRAM NAME: neptune_create_db_snapshot.py
PROGRAM POURPOSE: to demonstrate the creation of a db snapshot
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz

ripped from rds module
"""

import boto3

neptune = boto3.client('neptune', region_name='us-west-2')

def create_db_instance(db_snapshot_id, db_instance_id):
    response = neptune.create_db_snapshot(
        DBSnapshotIdentifier=db_snapshot_id,
        DBInstanceIdentifier=db_instance_id,
    )

    return response
