"""
PROGRAM NAME: r53_create_health_check.py
PROGRAM POURPOSE: creates a healthcheck for route53 using aws boto3
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""
import boto3

route53 = boto3.client('route53', region_name='us-west-2')

def r53_create_health_check(ip_address, port, type, resourcePath, Fully_qualified_domain_name, search_string, request_interval, faliure_threshold, mesure_latency:bool, disabled:bool, health_threshold, regions, alarm_region, alarm_names):
    response = route53.create_health_check(
        HealthCheckConfig={
            'IPAddress': ip_address,
            'Port': port,
            'Type': type,
            'ResourcePath': resourcePath,
            'FullyQualifiedDomainName': Fully_qualified_domain_name,
            'SearchString': search_string,
            'RequestInterval': request_interval,
            'FailureThreshold': faliure_threshold,
            'MeasureLatency': mesure_latency,
            'Disabled': disabled,
            'HealthThreshold': health_threshold,
            'Regions': [
                regions,
            ],
            'AlarmIdentifier': {
                'Region': alarm_region,
                'Name': alarm_names
            },
        }
    )
    return response
