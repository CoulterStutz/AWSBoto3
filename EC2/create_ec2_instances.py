"""
PROGRAM NAME: create_ec2_instances.py
PROGRAM PURPOSE: to create ec2 instances
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""


import boto3, botocore

client = boto3.client('ec2', region_name='us-west-2')

def create_ec2(instance_name, instance_type, min_Count, max_Count, volume_Size, volume_Type):
        response = client.run_instances(

            BlockDeviceMappings=[
                {
                    'DeviceName': instance_name,
                    'DeviceName': '/dev/xvda',
                    'Ebs': {

                        'DeleteOnTermination': True,
                        'VolumeSize': volume_Size,
                        'VolumeType': volume_Type
                    },
                },
            ],
            ImageId='ami-6cd6f714',
            InstanceType=instance_type,
            MaxCount=max_Count,
            MinCount=min_Count,
            Monitoring={
                'Enabled': False
            },
        )

        return response

if __name__ == "__main__":
    print(create_ec2(instance_name='MyInstance', instance_type='t2.micro', min_Count=1, max_Count=1, volume_Size=8, volume_Type='gp2'))
