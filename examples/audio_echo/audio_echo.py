from toxpython import Tox
from toxpython import ToxAVC
from toxpython import TOX_USER_STATUS_NONE
import time
import sys
from threading import Thread

# Todo:
# Recieve File and Echo it back (delete afterwards)
class EchoAudioClient(ToxAVC,Thread):

        running = False

	def __init__(self,tox):
                Thread.__init__(self)
                ToxAVC.__init__(self,tox)


        def stop(self):
            self.running = False
                                    
        def run(self):
            self.running = True
            while(self.running):
                self.iterate()
                time.sleep(self.sleepInterval()/1000.0)

            self.kill()



        def on_call(self,friend_number,audio_enabled,video_enabled):                                                                                                                 
            self.answer(friend_number,16000,16000)
            print("Incoming Call")
        
        def on_call_state(self,friend_number,state):                                                                                                                                 
            print("Call State Changed")

        def on_audio_recieve_frame(self,friend_number,width,height,y,u,v,ystride,ustride,vstride):                                                                                   
            print("Recieved audio Frame")

        def on_video_recieve_frame(self,friend_number,pcm,sample_count,channels,sampling_rate):
            print("Recieved video Frame")


class EchoClient(Tox,Thread):

        running = False
	def __init__(self):
	
                Thread.__init__(self)
		self.init("./userdata")
		self.setName("Echo Client")
		self.save("./userdata")
		self.set_status(TOX_USER_STATUS_NONE)

		print(self.get_address())

		self.bootstrap("104.219.184.206",443,"8CD087E31C67568103E8C2A28653337E90E6B8EDA0D765D57C6B5172B4F1F04C")


	def on_friend_request(self,public_key, message):
		self.friend_add_norequest(public_key)

		self.save("./userdata")
		print("Recieved Friend request")

	def on_connection_status(self,connection_status):
		print("Connected")

	def on_friend_message(self,friend_id, message_type,message):
		self.send_message(friend_id,message_type,message)

        def stop(self):
            self.running = False
                                    
        def run(self):
            self.running = True
            while(self.running):
                self.iterate()
                time.sleep(self.sleepInterval()/1000.0)

            self.kill()



client = EchoClient()
audio_client = EchoAudioClient(client._p)
client.start()
audio_client.start()

try:
	while True:
	    time.sleep(1)

except Exception,e:
	print str(e)
	traceback.print_stack(file=sys.stdout)

finally:
	client.stop()
	audio_client.stop()
	exit(1)


