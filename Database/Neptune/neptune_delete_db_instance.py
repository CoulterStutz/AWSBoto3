"""
PROGRAM NAME: neptune_delete_db_instance.py
PROGRAM PURPOSE: deletes a neptune graphical database
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
neptune = boto3.client('neptune', region_name='us-west-2')

def neptune_delete_db_instance(instance_id, skipFinalSnapshot: bool, finalSnapshotID=0):
    if skipFinalSnapshot == False:
        response = neptune.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=skipFinalSnapshot,
            FinalDBSnapshotIdentifier=finalSnapshotID,
        )
    else:
        response = neptune.delete_db_instance(
            DBInstanceIdentifier=instance_id,
            SkipFinalSnapshot=skipFinalSnapshot
        )

    return response


print(neptune_delete_db_instance('greg', skipFinalSnapshot=True))
