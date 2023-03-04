"""
PROGRAM NAME: start_document_classification_job.py
PROGRAM POURPOSE: tells aws comprehend to start a document class detection job
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

comprehend = boto3.client('comprehend', region_name='us-west-2')


def start_document_classification_job(input_s3_url, doc_reader_action, doc_reader_mode, feature_types, output_s3, jobname):
    response = comprehend.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': input_s3_url,
            'InputFormat': 'ONE_DOC_PER_FILE',
            'DocumentReaderConfig': {
                'DocumentReadAction': doc_reader_action,
                'DocumentReadMode': doc_reader_mode,
                'FeatureTypes': [
                    feature_types
                ]
            }
        },
        OutputDataConfig={
            'S3Uri': output_s3,
        },
        JobName=jobname
    )
    return response

print(start_document_classification_job(''))
