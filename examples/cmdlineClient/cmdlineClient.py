from toxpython import Tox
from toxpython import TOX_USER_STATUS_NONE
from threading import Thread
import time


class CMDLineClient(Tox,Thread):
    

    running = False 

    def __init__(self):

        Thread.__init__(self)
	self.init("./userdata")
	self.setName("Command Line Client")
	self.save("./userdata")
	self.set_status(TOX_USER_STATUS_NONE)

	print(self.get_address())


	self.bootstrap("104.219.184.206",443,"8CD087E31C67568103E8C2A28653337E90E6B8EDA0D765D57C6B5172B4F1F04C")

    def on_friend_request(self,public_key, message):
        # On friend request ask user if he wants to accept
	self.friend_add_norequest(public_key)
	self.save("./userdata")
	print("Recieved Friend request")

    def on_connection_status(self,connection_status):
        if(connection_status == True):
            print("Connected")
        else: 
            time.sleep(1)
            if(self.self_get_connection_status == False):
                print("Disconnected")
	        self.bootstrap("104.219.184.206",443,"8CD087E31C67568103E8C2A28653337E90E6B8EDA0D765D57C6B5172B4F1F04C")


    def on_friend_message(self,friend_id, message_type,message):
        print(str(self.friend_get_name(friend_id) + ": " + str(message)))

    def run(self):
        self.running = True
    	while(self.running):
            self.iterate()
    	    time.sleep(self.sleepInterval()/1000000.0)

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


client = CMDLineClient()
client.start()

try:
    while True:
        inp = raw_input(">")
        inplist = inp.split()
        if(len(inplist) < 1):
            continue

        cmd = inplist[0]

        if   (cmd == "add"):
            if(len(inplist) <2):
                print("Invalid Arguments")
                continue

            if (client.friend_add(inplist[1],"Invite Request") == True):
                print ("Adding friend: " + inplist[1])
	        self.save("./userdata")
            else:
                print ("Adding friend failed")
                


        elif (cmd == "del"):
            if(len(inplist) <2):
                print("Invalid Arguments")
                continue 

            print ("Deleting friend: " + inplist[1])
            client.friend_delete(inplist[1])
	    self.save("./userdata")


        elif (cmd == "msg"):
            if (len(inplist) <3):
                print("Invalid Arguments")
                continue

            message = ""
            i = 2
            for i in range (len(inplist)):
                message += " " 
                message += inplist[i]
            print ("Sending Message to " + inplist[1] + ": " + message)
            #client.send_message(friend,type,message)

        elif (cmd == "list"):
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

except KeyboardInterrupt:
    client.stop()
    exit(1)




















