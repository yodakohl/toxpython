import datetime
import time
import logging

from .ctox import *
from .util import *

import numpy as np
from numpy.lib import stride_tricks

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

            cb = toxav_call_cb(self.get_call_callback())
            self._av_fRefs.append(cb)
            toxav_callback_call(self._av_p, cb , py_object(self))

            cb = toxav_video_receive_frame_cb(self.get_video_recieve_frame_callback())
            self._av_fRefs.append(cb)
            toxav_callback_video_receive_frame(self._av_p, cb , py_object(self))

            cb = toxav_audio_receive_frame_cb(self.get_audio_recieve_frame_callback())
            self._av_fRefs.append(cb)
            toxav_callback_audio_receive_frame(self._av_p,cb,py_object(self))

            cb = toxav_bit_rate_status_cb(self.get_bit_rate_status_callback())
            self._av_fRefs.append(cb)
            toxav_callback_bit_rate_status(self._av_p,cb,py_object(self))

            cb = toxav_call_state_cb(self.get_call_state_callback())
            self._av_fRefs.append(cb)
            toxav_callback_call_state(self._av_p,cb,py_object(self))


    def av_iterate(self):
        if(self._av_p != None):
            toxav_iterate(self._av_p)

    def av_sleepInterval(self):
        if(self._av_p != None):
            return toxav_iteration_interval(self._av_p)

    def call(self,friend_number,audio_bit_rate,video_bit_rate):
        response = pointer(c_int())
        toxav_call(self._av_p, friend_number, audio_bit_rate,video_bit_rate, response); #bool
        print("Answer call" + str(response.contents.value))
        return  response.contents.value


    def answer(self,friend_number,audio_bit_rate,video_bit_rate):
        response = pointer(c_int())
        toxav_answer(self._av_p, friend_number, audio_bit_rate, video_bit_rate,response); #bool
        print("Answer response" + str(response.contents.value))
        return  response.contents.value

 
    def get_call_state_callback(self):
        def get_call_state_callback_tmp(toxav,friend_number,state,userdata):
            self.on_call_state(friend_number,state)
        return get_call_state_callback_tmp


    def get_bit_rate_status_callback(self):
        def bit_rate_status_callback_tmp(toxav,friend_number,audio_bit_rate,video_bit_rate,user_data):
            self.on_bit_rate_status(friend_number,audio_bit_rate,video_bit_rate)
        return bit_rate_status_callback_tmp



    def get_call_callback(self):
        def get_call_callback_tmp(toxav, friend_number, audio_enabled, video_enabled, userdata):
            logger.info('Recieved Call Callback from: %s'%(friend_number))
            self.on_call(friend_number,audio_enabled,video_enabled)
        return get_call_callback_tmp


    def get_video_recieve_frame_callback(self):

        def get_video_recieve_frame_callback_tmp(toxav,friend_number,width,height,y,u,v,ystride,ustride,vstride,userdata):
            Ylen = max(width,   abs(ystride)) *  height
            Ulen = max(width/2, abs(ustride)) * (height/2) 
            Vlen = max(width/2, abs(vstride)) * (height/2)

            y_data = np.ctypeslib.as_array(y,shape=(Ylen,))
            u_data = np.ctypeslib.as_array(u,shape=(Ulen,))
            v_data = np.ctypeslib.as_array(v,shape=(Vlen,))
 
            num_frames = height
            frame_length = width
            row_stride = ystride
            col_stride = 1
            strided_y = stride_tricks.as_strided(y_data,shape=(num_frames,frame_length), strides=(row_stride,col_stride))
            bufy = strided_y.ravel()

            num_frames = height/2
            frame_length = width/2
            row_stride = ustride
            col_stride = 1
            strided_u = stride_tricks.as_strided(u_data,shape=(num_frames,frame_length), strides=(row_stride,col_stride))
            bufu = strided_u.ravel()

            num_frames = height/2
            frame_length = width/2
            row_stride = vstride
            col_stride = 1
            strided_v = stride_tricks.as_strided(v_data,shape=(num_frames,frame_length), strides=(row_stride,col_stride))
            bufv = strided_v.ravel()

            self.on_video_recieve_frame(friend_number,width,height,bufy,bufu,bufv)
        return get_video_recieve_frame_callback_tmp


    def get_audio_recieve_frame_callback(self):
         def get_audio_recieve_frame_callback(toxav,friend_number,pcm, sample_count,channels,sample_rate,userdata):

             framesize = sample_count * channels *2 
             data = ptr_to_string(pcm,framesize)
             self.on_audio_recieve_frame(friend_number,data,sample_count,channels,sample_rate)
         return get_audio_recieve_frame_callback


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


    def on_bit_rate_status(self,friend_number,audio_bit_rate,video_bit_rate):
        pass

    def audio_send_frame(self,friend_number,pcm,sample_count,channels,sample_rate):
        response = pointer(c_int())

        data_pointer = pcm.ctypes.data_as(ctypes.POINTER(ctypes.c_int16))
        toxav_audio_send_frame(self._av_p, friend_number, data_pointer ,sample_count,channels,sample_rate, response) #bool

        if ( response.contents.value == TOXAV_ERR_SEND_FRAME_OK):
            return True
        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_FOUND:" + str(friend_number))
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_NULL):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_NULL")
            return False

        elif ( response.contents.value == TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL):
            logger.info("Cannot send audio frame:TOXAV_ERR_SEND_FRAME_FRIEND_NOT_IN_CALL" + str(friend_number))
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

        y_av_pointer = y.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
        u_av_pointer = u.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))
        v_av_pointer = v.ctypes.data_as(ctypes.POINTER(ctypes.c_uint8))

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
            print("Cannot send video frame")

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








