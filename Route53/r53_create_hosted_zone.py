"""
PROGRAM NAME: r53_create_hosted_zone.py
PROGRAM POURPOSE: Creates a hosted zone
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""
import boto3

route53 = boto3.client('route53', region_name='us-west-2')

def create_hosted_zone(zone_name, vpc_region, vpc_id, privatezone:bool, caller_reference):
    response = route53.create_hosted_zone(
        Name=zone_name,
        VPC={
            'VPCRegion': vpc_region,
            'VPCId': vpc_id
        },
        HostedZoneConfig={
            'PrivateZone': privatezone
        },
        CallerReference=caller_reference,
    )
    return response


print(create_hosted_zone('myzone', 'us-west-2', 'vpc-0a2a405c8a4b3ef79', False, 'helloworld'))
