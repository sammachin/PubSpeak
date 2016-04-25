from pubnub import Pubnub
from creds import *

def callback(message):
	print(message)	

def send(message):
	pubnub.publish('speak', message, callback=callback, error=callback)
		
	
if __name__ == "__main__":
	pubnub = Pubnub(publish_key=pubnubPubKey, subscribe_key=pubnubSubKey)
	send('Hello World')