"""
PROGRAM NAME: create_entity_reconizer.py
PROGRAM POURPOSE: tells aws comprehend to create a entity reconizer
DATE WRITTEN: 1/23/23
PROGRAMMER: Coulter C. Stutz
"""
import boto3

comprehend = boto3.client('comprehend', region_name='us-west-2')


def create_entity_reconizer(reconizer_name, version_name, rolearn, dataformat, entity_types, documents_s3_uri, doc_input_format, annotations_s3_uri,
                            entity_list, augmented_manifests, augmented_manifests_split, augmented_manifests_attributes_names, source_document_s3_uri,
                            source_document_type, client_request_token, language, volume_kms_id, vpc_security_group_ids, vpc_subnets, model_kms_key_id,
                            model_policy):

    response = comprehend.create_entity_recognizer(
        RecognizerName=reconizer_name,
        VersionName=version_name,
        DataAccessRoleArn=rolearn,
        InputDataConfig={
            'DataFormat': dataformat,
            'EntityTypes': [
                {
                    'Type': entity_types
                },
            ],
            'Documents': {
                'TestS3Uri': documents_s3_uri,
                'InputFormat': doc_input_format
            },
            'Annotations': {
                'S3Uri': annotations_s3_uri,
            },
            'EntityList': {
                'S3Uri': entity_list
            },
            'AugmentedManifests': [
                {
                    'S3Uri': augmented_manifests,
                    'Split': augmented_manifests_split,
                    'AttributeNames': [
                        augmented_manifests_attributes_names,
                    ],
                    'AnnotationDataS3Uri': annotations_s3_uri,
                    'SourceDocumentsS3Uri': source_document_s3_uri,
                    'DocumentType': source_document_type
                },
            ]
        },
        ClientRequestToken=client_request_token,
        LanguageCode=language,
        VolumeKmsKeyId=volume_kms_id,
        VpcConfig={
            'SecurityGroupIds': [
                vpc_security_group_ids,
            ],
            'Subnets': [
                vpc_subnets,
            ]
        },
        ModelKmsKeyId=model_kms_key_id,
        ModelPolicy=model_policy
    )
    return response

