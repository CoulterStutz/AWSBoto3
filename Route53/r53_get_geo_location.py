"""
PROGRAM NAME: r53_get_geo_location.py
PROGRAM POURPOSE: gets the geolocation
DATE WRITTEN: 1/26/23
Programmer: Coulter C. Stutz
"""

import boto3

route53 = boto3.client('route53', region_name='us-west-2')


def get_geo_location(continent_code, country_code, subdivision_code):
    response = route53.get_geo_location(
        ContinentCode=continent_code,
        CountryCode=country_code,
        SubdivisionCode=subdivision_code
    )
    return response
