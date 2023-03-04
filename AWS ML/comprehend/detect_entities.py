"""
PROGRAM NAME: detect_dominate_language.py
PROGRAM POURPOSE: tells aws comprehend to detect the dominate language in a given string
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

comprehend = boto3.client('comprehend', region_name='us-west-2')

def detect_entities(string):
    response = comprehend.batch_detect_entities(
        TextList=[
            string,
        ],
        LanguageCode='en'
    )
    return response

print(detect_entities('The quick brown fox jumped over the lazy dog'))
