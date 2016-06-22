import datetime
import time
import logging

from .ctox import *
from .util import *


logger = logging.getLogger('TOXAV')

class ToxAVC():

    _av_p = None
    _av_fRefs = []
    
    def __init__(self,ToxInstance):

        self._av_p = toxav_new (ToxInstance, None)
        self.av_registerCallbacks()  


    def av_registerCallbacks(self):
        logger.info('Register AV Callbacks')
        if(self._av_p != None):

            cb = toxav_call_cb(self.call_callback)
            self._av_fRefs.append(cb)
            toxav_callback_call(self._av_p, cb , py_object(self))

            cb = toxav_video_receive_frame_cb(self.video_recieve_frame_callback)
            self._av_fRefs.append(cb)
            toxav_callback_video_receive_frame(self._av_p, cb , py_object(self))

            cb = toxav_audio_receive_frame_cb(self.audio_recieve_frame_callback)
            self._av_fRefs.append(cb)
            toxav_callback_audio_receive_frame(self._av_p,cb,py_object(self))

            cb = toxav_bit_rate_status_cb(self.bit_rate_status_callback)
            self._av_fRefs.append(cb)
            toxav_callback_bit_rate_status(self._av_p,cb,py_object(self))

            cb = toxav_call_state_cb(self.call_state_callback)
            self._av_fRefs.append(cb)
            toxav_callback_call_state(self._av_p,cb,py_object(self))


    def av_iterate(self):
        if(self._av_p != None):
            toxav_iterate(self._av_p)

    def av_sleepInterval(self):
        if(self._av_p != None):
            return toxav_iteration_interval(self._av_p)

    def call(self,friend_number,audio_bit_rate,video_bit_rate):
        toxav_call(self._av_p, friend_number, audio_bit_rate,video_bit_rate, None); #bool


    def answer(self,friend_number,audio_bit_rate,video_bit_rate):
        toxav_answer(self._av_p, friend_number, audio_bit_rate, video_bit_rate,None); #bool


    @staticmethod 
    def call_state_callback(toxav,friend_number,state,userdata):
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
    def video_recieve_frame_callback(toxav,friend_number,width,height,y,u,v,ystride,ustride,vstride,userdata):
        logger.info('Recieved Video Frame Callback from: %s'%(friend_number))
        self = cast(userdata, py_object).value
        y_data = ptr_to_string(y,framesize)
        u_data = ptr_to_string(u,framesize)
        v_data = ptr_to_string(v,framesize)
        self.on_video_recieve_frame(friend_number,width,height,y_data,u_data,v_data,ystride,ustride,vstride)

    @staticmethod
    def audio_recieve_frame_callback(toxav,friend_number,pcm, sample_count,channels,sample_rate,userdata):
         self = cast(userdata, py_object).value
         framesize = sample_count * channels *2 
         data = ptr_to_string(pcm,framesize)
         self.on_audio_recieve_frame(friend_number,data,sample_count,channels,sample_rate)

    def on_call(self,friend_number,audio_enabled,video_enabled):
        pass

    def on_call_state(self,friend_number,state):
        pass

    def on_audio_recieve_frame(self, friend_number,pcm,sample_count,channels,sample_rate):
        pass
        

    def on_video_recieve_frame(self,friend_number,width,height,y,u,v,ystride,ustride,vstride):
        pass


    def call_control(self,friend_number,control):
        toxav_call_control(self._av_p,friend_number, control,None) #bool 

    def bit_rate_set(self,friend_number,audio_bit_rate,video_bit_rate):
        toxav_bit_rate_set(self._av_p,friend_number,audio_bit_rate,video_bit_rate, None) #bool 


    def on_bit_rate_status(friend_number,audio_bit_rate,video_bit_rate):
        pass

    def audio_send_frame(self,friend_number,pcm,sample_count,channels,sample_rate):
        response = pointer(c_int())
        buff = create_string_buffer(pcm,len(pcm))
        toxav_audio_send_frame(self._av_p, friend_number, buff ,sample_count,channels,sample_rate, response) #bool
        if ( response.contents.value == TOXAV_ERR_SEND_FRAME_OK):
            return True
        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_NULL):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_NULL")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_SYNC):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_SYNC")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_INVALID):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_INVALID")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_av_pAYLOAD_TYPE_DISABLED):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_av_pAYLOAD_TYPE_DISABLED")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_RTP_FAILED):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_RTP_FAILED")
            return False

        else:
            logger.info("Cannot send audio frame")
            return False


    def video_send_frame(self,friend_number,width,height,y,u,v):

        y_av_pointer = create_string_buffer(y,len(y))
        u_av_pointer = create_string_buffer(u,len(u))
        v_av_pointer = create_string_buffer(v,len(v))
        response = pointer(c_int())

        toxav_video_send_frame(self._av_p,friend_number, width, height, y_av_pointer, u_av_pointer, v_av_pointer,response) #bool
        if ( response.contents.value == TOXAV_ERR_SEND_FRAME_OK):
            return True
        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_NULL):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_NULL")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_SYNC):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_SYNC")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_INVALID):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_INVALID")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_av_pAYLOAD_TYPE_DISABLED):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_av_pAYLOAD_TYPE_DISABLED")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_RTP_FAILED):
            logger.info("Cannot send video frame:TOXAV_ERR_SEND_FRAME_RTP_FAILED")
            return False

        else:
            logger.info("Cannot send video frame")

    def add_av_groupchat(self):
        pass
        #int toxav_add_av_groupchat(Tox *tox, void (*audio_callback)(void *, int, int, const int16_t *, unsigned int, uint8_t,
        #                           unsigned int, void *), void *userdata);


    def join_av_groupchat(self,friend_number,data):
        pass

        #int toxav_join_av_groupchat(Tox *tox, int32_t friendnumber, const uint8_t *data, uint16_t length,
        #                            void (*audio_callback)(void *, int, int, const int16_t *, unsigned int, uint8_t, unsigned int, void *), void *userdata);

    def group_send_audio(self,groupnumber,pcm,samples,channels,sample_rate):
        pass
        #int toxav_group_send_audio(Tox *tox, int groupnumber, const int16_t *pcm, unsigned int samples, uint8_t channels,
        #                           unsigned int sample_rate);








