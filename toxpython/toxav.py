import datetime
import time
import logging

from .ctox import *
from .util import *


logger = logging.getLogger('TOXAV')

class ToxAV():

    _p = None
    _fRefs = []

    def init(self,ToxInstance):
        self._p = toxav_new (ToxInstance, 100) #max calls = 100

    def registerCallbacks(self):
        logger.debug('Register Callbacks')
        if(self._p != None):

            cb = toxav_call_cb(self.call_callback)
            self._fRefs.append(cb)
            toxav_callback_call(self._p, cb , py_object(self))

            cb = toxav_video_receive_frame_cb(self.video_recieve_frame_callback)
            self._fRefs.append(cb)
            toxav_callback_video_receive_frame(self._p, cb , py_object(self))

            cb = toxav_audio_receive_frame_cb(self.audio_recieve_frame_callback)
            self._fRefs.append(cb)
            toxav_callback_audio_receive_frame(self._p,cb,py_object(self))

            cb = toxav_bit_rate_status_cb(self.bit_rate_status_callback)
            self._fRefs.append(cb)
            toxav_bit_rate_status_cb(self._p,cb,py_object(self))

            cb = toxav_call_state_cb(self.call_state_callback)
            self._fRefs.append(cb)
            toxav_call_state_cb(self._p,cb,py_object(self))


    def iterate(self):
       toxav_iterate(self._p)

    def call(toxav,friend_number,audio_bit_rate,video_bit_rate):
        toxav_call(self._p, friend_number, audio_bit_rate,video_bit_rate, None); #bool


    def answer(toxav,friend_number,audio_bit_rate,video_bit_rate):
        toxav_answer(self._p, friend_number, audio_bit_rate, video_bit_rate,None); #bool


    @staticmethod 
    def call_state_callback(toxav,friend_number,state,user_data):
        self = cast(userdata, py_object).value
        self.on_call_state(friend_number,state)


    @staticmethod
    def bit_rate_status_callback(toxav,friend_number,audio_bit_rate,video_bit_rate,userdata):
        self = cast(userdata, py_object).value
        self.on_bit_rate_status(friend_number,audio_bit_rate,video_bit_rate)


    @staticmethod
    def call_callback(toxav, friend_number, audio_enabled, video_enabled, userdata):
        logger.info('Recieved Call Callback from: %s'%(friend_number))
        self = cast(userdata, py_object).value
        self.on_call(friend_number,audio_enabled,video_enabled)

    @staticmethod
    def video_receive_frame_callback(toxav,friend_number,width,height,y,u,v,ystride,ustride,vstride,userdata):
        logger.info('Recieved Video Frame Callback from: %s'%(friend_number))
        self = cast(userdata, py_object).value
        self.on_video_recieve_frame()
        #typedef void toxav_video_receive_frame_cb(ToxAV *toxAV, uint32_t friend_number, uint16_t width,
        #    uint16_t height, const uint8_t *y, const uint8_t *u, const uint8_t *v,
        #    int32_t ystride, int32_t ustride, int32_t vstride, void *user_data);

    @staticmethod
    def audio_recieve_frame_callback(toxav,friend_number,pcm, sample_count,channels,sample_rate,userdata):
         self = cast(userdata, py_object).value
         self.on_audio_recieve_frame()
         # typedef void toxav_audio_receive_frame_cb(ToxAV *toxAV, uint32_t friend_number, const int16_t *pcm,
         #    size_t sample_count, uint8_t channels, uint32_t sampling_rate,
         #    void *user_data);



    def on_call(friend_number,audio_enabled,video_enabled):
        pass

    def on_call_state(friend_number,state):
        pass

    def on_audio_recieve_frame(friend_number,width,height,y,u,v,ystride,ustride,vstride):
        pass
        

    def on_video_recieve_frame(friend_number,pcm,sample_count,channels,sampling_rate):
        pass


    def call_control(self,friend_number,control):
        toxav_call_control(self._p,friend_number, control,None) #bool 

    def bit_rate_set(self,friend_number,audio_bit_rate,video_bit_rate):
        toxav_bit_rate_set(self._p,friend_number,audio_bit_rate,video_bit_rate, None) #bool 


    def on_bit_rate_status(friend_number,audio_bit_rate,video_bit_rate):
        pass

    def audio_send_frame(self,friend_number,pcm,sample_count,channels,sample_rate):
        #toxav_audio_send_frame(self._p, friend_number, const int16_t *pcm,sample_count,channels,sampling_rate, None) #bool


    def video_send_frame(self,friend_number,width,height,y,u,v):
        #toxav_video_send_frame(self._ps,friend_number, width, height, const uint8_t *y, const uint8_t *u, const uint8_t *v,None) #bool


    def add_av_groupchat(self):
        #int toxav_add_av_groupchat(Tox *tox, void (*audio_callback)(void *, int, int, const int16_t *, unsigned int, uint8_t,
        #                           unsigned int, void *), void *userdata);


    def join_av_groupchat(self,friend_number,data):

        #int toxav_join_av_groupchat(Tox *tox, int32_t friendnumber, const uint8_t *data, uint16_t length,
        #                            void (*audio_callback)(void *, int, int, const int16_t *, unsigned int, uint8_t, unsigned int, void *), void *userdata);

    def group_send_audio(self,groupnumber,pcm,samples,channels,sample_rate):
        #int toxav_group_send_audio(Tox *tox, int groupnumber, const int16_t *pcm, unsigned int samples, uint8_t channels,
        #                           unsigned int sample_rate);








