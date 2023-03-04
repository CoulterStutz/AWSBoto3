"""
PROGRAM NAME: rds_create_instance.py
PROGRAM POURPOSE: to demonstrate the creation of RDS instances
DATE WRITTEN: 1/12/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

rds = boto3.client('rds', region_name='us-west-2')


def create_instance(database, db_name, instance_type, storage, max_instance_storage, instance_storage_class,
                    publically_accessable: bool, engine, master_username, master_password, deletion_protection: bool,
                    backup_retention_period, port, multi_az: bool, engine_version, auto_upgrading_engine: bool,
                    storage_encrypted: bool):
    response = rds.create_db_instance(
        DBName=database,
        DBInstanceIdentifier=db_name,
        DBInstanceClass=instance_type,
        AllocatedStorage=storage,
        Engine=engine,
        MasterUsername=master_username,
        MasterUserPassword=master_password,
        BackupRetentionPeriod=backup_retention_period,
        Port=port,
        MultiAZ=multi_az,
        EngineVersion=engine_version,
        AutoMinorVersionUpgrade=auto_upgrading_engine,
        PubliclyAccessible=publically_accessable,
        Tags=[
            {
                'Key': 'name',
                'Value': db_name
            },
        ],
        StorageEncrypted=storage_encrypted,
        DeletionProtection=deletion_protection,
        MaxAllocatedStorage=max_instance_storage,
    )

    return response

