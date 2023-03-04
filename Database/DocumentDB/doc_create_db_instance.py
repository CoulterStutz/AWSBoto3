"""
PROGRAM NAME: doc_create_db_instance.py
PROGRAM POURPOSE: creates a document db instance
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

document_db = boto3.client('docdb', region_name='us-west-2')

def create_document_db_instance(instance_id, db_instance_class, engine, minor_version_upgrade: bool, dbclusterid):
    response = document_db.create_db_instance(
        DBInstanceIdentifier=instance_id,
        DBInstanceClass=db_instance_class,
        Engine=engine,
        # AvailabilityZone='string',
        AutoMinorVersionUpgrade=minor_version_upgrade,
        Tags=[
            {
                'Key': 'name',
                'Value': instance_id
            },
        ],
        DBClusterIdentifier=dbclusterid
    )

