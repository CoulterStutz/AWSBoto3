"""
PROGRAM NAME: r53_get_health_count.py
PROGRAM POURPOSE: gets a count of health check policies
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""

import boto3
route53 = boto3.client('route53', region_name='us-west-2')

def get_health_count():
    response = route53.get_health_check_count()
    return response
