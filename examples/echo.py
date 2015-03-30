from toxpython import Tox
from toxpython import TOX_USER_STATUS_NONE
import time


class EchoClient(Tox):

	def __init__(self):
	
		self.init("./userdata")
		self.setName("Echo Client")
		self.save("./userdata")
		self.set_status(TOX_USER_STATUS_NONE)

		print(self.get_address())

		self.bootstrap("23.226.230.47",33445,"A09162D68618E742FFBCA1C2C70385E6679604B2D80EA6E84AD0996A1AC8A074")


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
			time.sleep(self.sleepInterval()/1000000.0)


client = EchoClient()
client.run()
