from toxpython import Tox
from toxpython import ToxAVC
from toxpython import TOX_USER_STATUS_NONE
import time
import sys
from threading import Thread
from audiostream import get_output
from audiostream import AudioSample
from array import array
from audiostream.sources.wave import SineSource


import pyaudio
p = pyaudio.PyAudio()
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100




class EchoAudioClient(ToxAVC,Thread):

        dev = None
        running = False
        stream = None
        sample = None
        mic_stream = None

    def __init__(self,tox):
                Thread.__init__(self)
                ToxAVC.__init__(self,tox)


        def stop(self):
            self.running = False

        def run(self):
            self.running = True
            while(self.running):
                self.iterate()
                time.sleep(self.sleepInterval()/10000.0)
                #if(self.mic_stream):
                #    data = self.mic_stream.read(CHUNK)
                #    print("Got Data : " + str(len(data)))

            self.kill()



        def on_call(self,friend_number,audio_enabled,video_enabled): 
            self.answer(friend_number,200,1024)
            self.mic_stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


            print("Incoming Call")
        
        def on_call_state(self,friend_number,state): 
            print("Call State Changed")

        def on_audio_recieve_frame(self, friend_number,data,sample_count,channels,sample_rate): 
            print("Recieved audio Frame: " + str(sample_count) + " " + str(channels) + " " + str(sample_rate))

            if(self.stream == None):
                self.stream = get_output(channels=channels, rate=sample_rate, buffersize=5)
                self.sample = AudioSample()
                self.stream.add_sample(self.sample)
                self.sample.play()

            self.sample.write(data)


        def on_video_recieve_frame(self,friend_number,width,height,y,u,v,ystride,ustride,vstride):
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


