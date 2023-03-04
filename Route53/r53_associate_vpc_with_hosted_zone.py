"""
PROGRAM NAME: r53_associate_vpc_with_hosted_zone.py
PROGRAM POURPOSE: To associate a vpc to a route53 dns hosted zone
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""
import boto3

route53 = boto3.client('route53', region_name='us-west-2')


def assosiate_vpc_with_r53(hostedzoneid, vpc_region, vpc_id):
    response = route53.associate_vpc_with_hosted_zone(
        HostedZoneId=hostedzoneid,
        VPC={
            'VPCRegion': vpc_region,
            'VPCId': vpc_id
        },
    )

    return response
