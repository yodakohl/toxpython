from toxpython import Tox
from toxpython import TOX_USER_STATUS_NONE
from toxpython import TOX_MESSAGE_TYPE_NORMAL

from threading import Thread
import time
from fileTransfer import FiletransferList
import os.path
import traceback

import sys


class CMDLineClient(Tox,Thread):

	fileTransferHandler = None
	running = False

	def __init__(self,path):
		Thread.__init__(self)
		self.datapath = path
                print("Using data path: " + str(self.datapath))
		self.init(self.datapath )
		self.setName("Command Line Client")
		self.save(self.datapath )
		self.set_status(TOX_USER_STATUS_NONE)
		self.fileTransferHandler = FiletransferList(self)
		print(self.get_address())

		self.bootstrap("195.154.119.113",33445,"E398A69646B8CEACA9F0B84F553726C1C49270558C57DF5F3C368F05A7D71354")
		if(self.self_get_connection_status() == False):
			print("Disconnected")
		else:
			print("Connected")

	def on_friend_request(self,public_key, message):
		#TODO: On friend request ask user if he wants to accept
		self.friend_add_norequest(public_key)
		self.save(self.datapath)
		print("Recieved Friend request")

	def on_connection_status(self,connection_status):
		if(self.self_get_connection_status() == True):
			print("Connected")
		else:
			print("Disconnected")
			time.sleep(1)
			if(self.self_get_connection_status() == False):
				print("Disconnected")
				self.bootstrap("195.154.119.113",33445,"E398A69646B8CEACA9F0B84F553726C1C49270558C57DF5F3C368F05A7D71354")

	def on_friend_message(self,friend_id, message_type,message):
		print(self.friend_get_name(friend_id) + ": " + message)

	def run(self):
		self.running = True
		while(self.running):
			self.iterate()
			time.sleep(self.sleepInterval()/1000.0)

		self.kill()

	def on_file_chunk_request(self,friend_number,file_number,position,length):
		self.fileTransferHandler.file_chunk_request(friend_number,file_number,position,length)

	def on_file_recv_control(self,friend_number, file_number,control):
		self.fileTransferHandler.file_recv_control(friend_number,file_number,control)

	def on_file_recv_chunk(self,friend_number,file_number,position,data):
		self.fileTransferHandler.file_recv_chunk(friend_number,file_number,position,data)

	def on_file_recv(self,friend_number,file_number,kind,file_size,filename):
		#set callback
		self.fileTransferHandler.recieveFile(friend_number,file_number,filename,file_size,self.on_file_transfer_finished)

	def on_file_transfer_finished(self,status):
		print("File transfer finished")

	def stop(self):
		self.running = False
		pass

	def print_help(self):
		print("Usage:")
		print("Add friend: add <key>")
		print("Delete friend: del <key>")
		print("Send Message: msg <friend> <message>")
		print("List friends: list")
		print("Send file:  file <friend> <path>")
		print("Exit: exit")
		print("Help: help")


print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

path= "./userdata"
if(len(sys.argv) == 2):
	path = str(sys.argv[1])

client = CMDLineClient(path)
client.start()

try:
	while True:
		inp = raw_input(">")
		inplist = inp.split()
		if(len(inplist) < 1):
			continue

		cmd = inplist[0]

		if (cmd == "add"):
			if(len(inplist) <2):
				print("Invalid Arguments")
				continue

			if (client.friend_add(inplist[1],"Invite Request") == True):
				print ("Adding friend successful: " + inplist[1])
			else:
				print ("Adding friend failed")

			client.save(client.datapath)

		elif (cmd == "del" or cmd == "rm"):
			if(len(inplist) <2):
				print("Invalid Arguments")
				continue

			print ("Deleting friend: " + inplist[1])
			try:
				client.friend_delete(int(inplist[1]))
			except:
				print("Couldn't delete friend")
			client.save("./userdata")

		elif (cmd == "msg"):
			if (len(inplist) <3):
				print("Invalid Arguments")
				continue

			message = inplist[2]

			for i in range (3,len(inplist)):
				message += " "
				message += inplist[i]
			print ("Sending Message to " + inplist[1] + ": " + message)
			client.send_message(int(inplist[1]),0,message)

		elif (cmd == "file" or cmd == "cp"):
			if (len(inplist) <3):
				print("Invalid Arguments")
				continue
			if not os.path.isfile(inplist[2]):
				print("File does not exist")
				continue
			print("Sending File " + inplist[2] + " to " + client.friend_get_name(int(inplist[1])))

			client.fileTransferHandler.addFileTransfer(int(inplist[1]),inplist[2])

		elif (cmd == "list" or cmd == "ls"):
			print ("Showing friend list ")
			friendList = client.get_friend_list()
			for friend in friendList:
				print(str(friend) + " " + client.friend_get_name(friend))

		elif (cmd == "exit"):
			print ("Terminating .. ")
			client.stop()
			exit(0)
		elif (cmd == "help"):
			client.print_help()
		else:
			print ("Unknown command")

except Exception,e:
	print str(e)
	traceback.print_stack(file=sys.stdout)

finally:
	client.stop()
	exit(1)
