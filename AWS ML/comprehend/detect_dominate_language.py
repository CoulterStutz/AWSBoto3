"""
PROGRAM NAME: detect_dominate_language.py
PROGRAM POURPOSE: tells aws comprehend to detect the dominate language in a given string
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

comprehend = boto3.client('comprehend', region_name='us-west-2')

def detect_dominate_language(string):
    response = comprehend.batch_detect_dominant_language(
        TextList=[
            string,
        ]
    )
    return response

print(detect_dominate_language('Hello World!'))
