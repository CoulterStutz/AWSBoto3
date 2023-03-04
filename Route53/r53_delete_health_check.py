"""
PROGRAM NAME: r53_delete_health_check.py
PROGRAM POURPOSE: deletes a healthcheck for route53 using aws boto3
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""
import boto3
route53 = boto3.client('route53', region_name='us-west-2')

def delete_health_check(health_check_id):
    response = route53.delete_health_check(
        HealthCheckId=health_check_id
    )
    return response
