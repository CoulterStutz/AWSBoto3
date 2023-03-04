"""
PROGRAM NAME: detect_key_phrases.py
PROGRAM POURPOSE: tells aws comprehend to create a entity reconizer
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3
comprehend = boto3.client('comprehend', region_name='us-west-2')

def detect_key_phrases(string, language):
    response = comprehend.batch_detect_key_phrases(
        TextList=[
            string,
        ],
        LanguageCode=language
    )
    return response

print(detect_key_phrases('hello world', 'en'))
