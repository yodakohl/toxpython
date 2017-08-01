from toxpython import Tox
from toxpython import TOX_USER_STATUS_NONE
import time
import logging
import sys
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

# Todo:
# Recieve File and Echo it back (delete afterwards)

class EchoClient(Tox):

	def __init__(self):
	
		Tox.__init__(self,"./userdata")
		self.setName("Echo Client")
		self.save("./userdata")
		self.set_status(TOX_USER_STATUS_NONE)

		print(self.get_address())

		self.AutoBootstrap()


	def on_friend_request(self,public_key, message):
		self.friend_add_norequest(public_key)
		self.save("./userdata")
		print("Recieved Friend request")

	def on_connection_status(self,connection_status):
		print("Connected")

	def on_friend_message(self,friend_id, message_type,message):
		self.send_message(friend_id,message_type,message)

	def run(self):
		while(True):
			self.iterate()
			time.sleep(self.sleepInterval()/100000.0)


client = EchoClient()
client.run()
