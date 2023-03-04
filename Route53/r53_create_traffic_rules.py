"""
PROGRAM NAME: r53_create_traffic_rules.py
PROGRAM POURPOSE: creates traffic rules for route53 using aws boto3
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""
import boto3

route53 = boto3.client('route53', region_name='us-west-2')

def create_traffic_policy(name, document, comment=0):
    response = route53.create_traffic_policy(
        Name=name,
        Document=document,
        Comment=comment
    )
    return response
