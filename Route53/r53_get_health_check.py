"""
PROGRAM NAME: r53_get_health_check.py
PROGRAM POURPOSE: gets a preconfigured healthcheck
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""

import boto3

route53 = boto3.client('route53', region_name='us-west-2')

def get_health_check(health_check_id):
    response = route53.get_health_check(
        HealthCheckId=health_check_id
    )
