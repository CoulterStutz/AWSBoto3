"""
PROGRAM NAME: rds_delete_db_snapshot.py
PROGRAM POURPOSE: to demonstrate the deletion of a db snapshot
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

rds = boto3.client('rds', region_name='us-west-2')

def create_db_instance(db_snapshot_id):
    response = rds.delete_db_snapshot(
        DBSnapshotIdentifier=db_snapshot_id,
    )

    return response
