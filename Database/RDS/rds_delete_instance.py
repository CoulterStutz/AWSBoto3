"""
PROGRAM NAME: rds_delete_db_instance.
PROGRAM POURPOSE: to demonstrate the deleting of a rds instance
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

rds = boto3.client('rds', region_name='us-west-2')


def rds_delete_db_instance(instance_id, skipFinalSnapshot: bool, deleteAutoBackups: bool, finalSnapshotID=0):
    if skipFinalSnapshot == False:
        response = rds.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=skipFinalSnapshot,
            FinalDBSnapshotIdentifier=finalSnapshotID,
            DeleteAutomatedBackups=deleteAutoBackups
        )
    else:
        response = rds.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=skipFinalSnapshot,
            DeleteAutomatedBackups=deleteAutoBackups
        )

    return response


