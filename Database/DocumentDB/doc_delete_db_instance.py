"""
PROGRAM NAME: doc_delete_db_instance.py
PROGRAM POURPOSE: deletes a document db instance
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3

document_db = boto3.client('docdb', region_name='us-west-2')

def delete_document_db_instance(instance_id):
    response = document_db.delete_db_instance(
        DBInstanceIdentifier=instance_id
    )
