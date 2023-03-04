"""
PROGRAM NAME: waf_associate_web_acl.py
PROGRAM POURPOSE:
DATE WRITTEN 1/26/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3
waf = boto3.client('wafv2')

def associate_web_acl(web_acl_arn, resource_arn):
    response = waf.associate_web_acl(
        WebACLArn=web_acl_arn,
        ResourceArn=resource_arn
    )
