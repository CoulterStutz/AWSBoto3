"""
PROGRAM NAME: r53_delete_hosted_zone.py
PROGRAM POURPOSE: deletes a hosted zone
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""

import boto3
route53 = boto3.client('route53', region_name='us-west-2')

def get_hosted_zone(hosted_zone_id):
    response = route53.get_hosted_zone(
        Id=hosted_zone_id
    )
    return response
