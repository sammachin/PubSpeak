import pyvona
from creds import *
import os
from pubnub import Pubnub
import tempfile
import signal
import sys


voice = 'Emma'

def say(text):
	v = pyvona.create_voice(ivonaAccessKey, ivonaSecretKey)
	v.codec = 'mp3'
	v.voice_name = voice
	v.region = 'eu-west'
	tf = tempfile.NamedTemporaryFile(suffix=".mp3")
	v.fetch_voice(text, tf.name)
	os.system('mpg123 -q {}'.format(tf.name))
	tf.close()


def callback(message, channel):
	print("MESSAGE RECEIVED")
	print(message)
	if channel == 'speak':
		say(message)


def error(message):
	print("ERROR")
	print(message)
	

def connect(message):
	print("CONNECTED")
	print(message)


def signal_handler(signal, frame):
	print('You pressed Ctrl+C!')
	pubnub.unsubscribe(channel='speak')
	sys.exit(0)


if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	pubnub = Pubnub(publish_key=pubnubPubKey, subscribe_key=pubnubSubKey)
	pubnub.subscribe(channels="speak", callback=callback, error=error, connect=connect)