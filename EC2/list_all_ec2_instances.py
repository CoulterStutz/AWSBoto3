"""
PROGRAM NAME: list_all_ec2_instances
PROGRAM PURPOSE: to list ec2 instances
DATE WRITTEN: 1/6/23
PROGRAMMER: Coulter C. Stutz
"""

import os
try:
    from termcolor import colored
    import boto3, botocore
except ModuleNotFoundError:
    os.system('pip3 install termcolor')
    os.system('pip3 install boto3')

terminated = []
running = []
stopped = []

ec2 = boto3.client('ec2', region_name='us-west-2')
response = ec2.describe_instances()
def list_ec2_instances():
    for reservation in response["Reservations"]:

        for instance in reservation["Instances"]:

            instance_state = instance["State"]

            if instance_state["Name"] == 'terminated':
                terminated.append(instance)
            elif instance_state["Name"] == 'running':
                running.append(instance)
            elif instance_state["Name"] == 'stopped':
                stopped.append(instance)

    if len(running) != 0:
        print(colored('Running!', 'green'))
        for x in running:
            print(f'     {x["InstanceId"]}')


    if len(stopped) != 0:
        print(colored('Stopped', 'red'))
        for x in stopped:
            print(f'     {x["InstanceId"]}')


    if len(terminated) != 0:
        print(colored('Terminated', 'gray'))
        for x in terminated:
            print(f'     {x["InstanceId"]}')


list_ec2_instances()
