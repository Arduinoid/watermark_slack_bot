'''
Main script for running the Slack chat bot. So far it's use will be
contained to producing multiple watermarked images.
'''
from __future__ import print_function
import os
import re
import time
from slackclient import SlackClient
from watermark import *

SLACK_TOKEN = os.getenv('SLACK_BOT_TOKEN')
BOT_ID = str(os.getenv('BOT_ID'))

AT_BOT = "<@" + BOT_ID + ">"
COMMANDS = {'make': 0}

slack_client = SlackClient(SLACK_TOKEN)


def handle_command(command, channel, user):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Hey there! Use the *" \
               + COMMANDS.keys()[0] + \
               """* command along with a number, delimited by a space.
                I can then go ahead and get some stuff done for ya :wink:\n
               Example: `@waterboy make 500` will make 500 watermarked images"""
    # Determine which command the user is requesting to use
    if command.startswith('make'):
        ex = r'\d+'
        match = re.search(ex, command)
        amount = match.group(0)
        if int(amount) <= 700:
            image_files = get_image_files(LOCATION)
            img_file = pick_image_from(image_files)
            if img_file[0] is not None:
                out_directory = img_file[1] + 'watermarked_' + img_file[0].split('.')[0]
                response = "Alright, I'm on it. Making " + amount + " copies of " + img_file[0] + " image file..."
                try:
                    os.mkdir(out_directory)
                    slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
                    multi_watermark(img_file,int(amount))
                    response = "OK, you're all set @{}".format(get_user_name(user))
                except:
                    response = "Oops, looks like there's already a folder here with these pictures\nTry removing the old folder first and run the command again. :ghost:"
                slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
            else:
                response = "I'm not seeing an image in the directory, perhaps you didn't put one there?"
                slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
        else:
            response = "I can understand you want a lot of images, but lets try to keep it to less than 700, OK :grimacing:"
            slack_client.api_call("chat.postMessage", channel=channel,text=response, as_user=True)
    else:
        slack_client.api_call("chat.postMessage", channel=channel,
                              text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, BASEd on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel'], output['user']
    return None, None, None


def get_user_name(user_id):
    users = (slack_client.api_call('users.list')).get('members')
    for i in users:
        if i['id'] == user_id:
            return i['name']
    return None


if __name__ == '__main__':
    READ_WEBSOCKET_DELAY = 1
    if slack_client.rtm_connect():
        print("multi_watermark bot connected and running")
        while True:
            command, channel, user = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel, user)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection faild. Invalid Slack token or bot ID?")
