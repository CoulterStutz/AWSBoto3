"""
PROGRAM NAME: neptune_create_db_instance.py
PROGRAM PURPOSE: Creates a neptune graphical database
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

neptune = boto3.client('neptune', region_name='us-west-2')


def neptune_create_db_instance(db_name, db_instance_id, db_instance_class, allocated_storage, storage_type,
                               storage_encrypted: bool, deletion_protection: bool, Engine, master_username,
                               master_password, backup_retention_period, port, multiAZ: bool, EngineVersion,
                               autoUpgradeEngine: bool, public: bool):

    response = neptune.create_db_instance(
        DBName=db_name,
        DBInstanceIdentifier=db_instance_id,
        AllocatedStorage=allocated_storage,
        DBInstanceClass=db_instance_class,
        Engine=Engine,
        MasterUsername=master_username,
        MasterUserPassword=master_password,

        BackupRetentionPeriod=backup_retention_period,
        Port=port,
        MultiAZ=multiAZ,
        EngineVersion=EngineVersion,
        AutoMinorVersionUpgrade=autoUpgradeEngine,
        PubliclyAccessible=public,
        Tags=[
            {
                'Key': 'name',
                'Value': db_name
            },
        ],
        StorageType=storage_type,
        StorageEncrypted=storage_encrypted,
        DeletionProtection=deletion_protection
    )

    return response

