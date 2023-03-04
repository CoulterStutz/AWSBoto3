"""
PROGRAM NAME: start_topic_detection_job.py
PROGRAM POURPOSE: tells aws comprehend to start a topic detection job
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

comprehend = boto3.client('comprehend', region_name='us-west-2')


def start_topic_detection_job(input_s3_url, doc_reader_action, doc_reader_mode, output_s3, jobname,
                              num_of_topics: int, arn):
    response = comprehend.start_topics_detection_job(
        InputDataConfig={
            'S3Uri': input_s3_url,
            'InputFormat': 'ONE_DOC_PER_FILE',
            'DocumentReaderConfig': {
                'DocumentReadAction': doc_reader_action,  # 'TEXTRACT_DETECT_DOCUMENT_TEXT'|'TEXTRACT_ANALYZE_DOCUMENT'
                'DocumentReadMode': doc_reader_mode,  # 'SERVICE_DEFAULT'|'FORCE_DOCUMENT_READ_ACTION'
            }
        },
        OutputDataConfig={
            'S3Uri': output_s3,
        },
        JobName=jobname,
        NumberOfTopics=num_of_topics,
        DataAccessRoleArn=arn
    )
    return response


print(start_topic_detection_job(
    's3://repositorypython/AWS/AWS ML/comprehend/testcases/mario_becomes_homeless_chatgpt_test_case.txt',
    'TEXTRACT_ANALYZE_DOCUMENT', doc_reader_mode='SERVICE_DEFAULT', output_s3='s3://repositorypython/AWS/AWS ML/comprehend/testcases/out.txt',
    jobname='mariosonicredpill', num_of_topics=1, arn='arn:aws:s3:::repositorypython'))
