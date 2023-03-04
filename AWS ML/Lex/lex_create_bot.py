"""
PROGRAM NAME: lex_create_bot.py
PROGRAM POURPOSE: Creates a lex chat bot
DATE WRITTEN: 1/13/22
PROGRAMMER: Coulter C. Stutz
"""

import boto3

lex = boto3.client('lexv2-models', region_name='us-west-2')
def lex_create_bot(bot_name, description, COPPA_Complience:bool, idle_session_time, roleArn):
        response = lex.create_bot(
            botName=bot_name,
            description=description,
            roleArn=roleArn,
            dataPrivacy={
                'childDirected': COPPA_Complience
            },
            idleSessionTTLInSeconds=idle_session_time,
        )
        return response
