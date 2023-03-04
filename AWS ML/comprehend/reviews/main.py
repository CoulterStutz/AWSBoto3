"""
PROGRAM NAME: main.py (reviews)
PROGRAM POURPOSE: to be able to decipher between a good and bad review, then sort them into the according documents
DATE WRITTEN: 1/5/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3
import json

comprehend = boto3.client('comprehend', region_name='us-west-2')

reviews = open('reviews.txt', 'r+')

good_reviews = []
bad_reviews =  []
neutral_reviews = []
mixed_reviews = []

for x in reviews:
    response = comprehend.batch_detect_sentiment(
        TextList=[
            x,
        ],
        LanguageCode='en'
    )

    """for x in range(len(str(response))):  For tuning the output listener for your environment
        print(f'{x}:{str(response)[x]}')"""

    print(response)

    if str(response)[43] == 'P':
        good_reviews.append(x)
    elif str(response)[43] == 'N':
        if str(response)[45] == 'U':
            neutral_reviews.append(x)
        else:
            bad_reviews.append(x)
    elif str(response)[43] == 'M':
        mixed_reviews.append(x)

good_file = open('good.txt', 'w+')
bad_file = open('bad.txt', 'w+')

if len(neutral_reviews) != 0:
    neutral_file = open('neutral.txt', 'w+')
    neutral_file.write(''.join(neutral_reviews))

if len(mixed_reviews) != 0:
    mixed_file = open('mixed.txt', 'w+')
    mixed_file.write(''.join(mixed_reviews))


print('\n')
print(good_reviews)
print(bad_reviews)
print(neutral_reviews)


good_file.write(''.join(good_reviews))
bad_file.write(''.join(bad_reviews))

average = len(good_reviews) + len(bad_reviews) + len(mixed_reviews) + len(neutral_reviews)
print()

if len(good_reviews) != 0:
    print(f'Good Reviews:{len(good_reviews)/average}')

if len(bad_reviews) != 0:
    print(f'Bad Reviews:{len(bad_reviews)/average}')

if len(mixed_reviews) != 0:
    print(f'Mixed Reviews:{len(mixed_reviews)/average}')

if len(neutral_reviews) != 0:
    print(f'Neutral Reviews:{len(mixed_reviews)/average}')
