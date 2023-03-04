"""
PROGRAM NAME: doc_start_cluster_db.py
PROGRAM POURPOSE: starts a cluster db
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""

import boto3
document_db = boto3.client('docdb', region_name='us-west-2')


def doc_db_start_cluster(db_cluster_id):
    response = document_db.start_db_cluster(
        DBClusterIdentifier=db_cluster_id
    )
