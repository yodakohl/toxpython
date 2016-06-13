import datetime
import time
import logging

from .ctox import *
from .util import *

## Todo: Proper error handling
## Todo: Implement missing API

logger = logging.getLogger('TOX')

class ToxAV():

    _p = None

    def init(self,ToxInstance):
        self._p = toxav_new (ToxInstance, 100) #max calls = 100


class Tox():

    _p = None

    _fRefs = []

    def init(self,fileName=None, options=None):

        mbuffer = None
        userdata = None
        datalen = 0
        if( fileName != None):
            try:
                with open(fileName, 'rb') as f:
                    userdata = f.read()
                    datalen = len(userdata)
                    mubb = create_string_buffer(userdata,datalen)
                    mbuffer = cast(mubb, POINTER(c_uint8)).contents

            except Exception as e:
                logger.warning("Error loading savedata: " +str(e) )


        defaults = {
            'ipv6_enabled': True,
            'udp_disabled': False,
            'proxy_type': TOX_PROXY_TYPE_NONE,
            'proxy_host': '',
            'proxy_port': 0,
            'start_port': 0,
            'tcp_port' : 0,
            'end_port': 33545,
        }

        if(options == None):
            options = defaults

        opt = Tox_Options()
        #for k, v in defaults.items():
        #   if k not in options:
        #       options[k] = v
        opt.ipv6_enabled = c_bool(True)
        opt.udp_enabled = c_bool(True)
        opt.proxy_type = TOX_PROXY_TYPE_NONE
        opt.proxy_host = String(None)
        opt.proxy_port = 0
        opt.start_port = 0
        opt.end_port = 0

        if(mbuffer != None):
            opt.savedata_type = TOX_SAVEDATA_TYPE_TOX_SAVE
            opt.savedata_data = pointer(mbuffer)
            opt.savedata_length = datalen
        else:
            opt.savedata_type = TOX_SAVEDATA_TYPE_NONE

        response = pointer(c_int(9))
        self._p = tox_new(pointer(opt),response)

        if response.contents.value != TOX_ERR_NEW_OK:
            logger.error("Tox init failed: %s"%response.contents.value)
        self.registerCallbacks()


    def save(self,fileName):
        logger.info('Saving to: %s'%fileName)
        buffersize = tox_get_savedata_size(self._p)
        userdata = create_string_buffer(buffersize)
        tox_get_savedata(self._p,userdata)
        with open(fileName, 'w+b') as f:
            f.write(userdata.raw)

    def iterate(self):
        tox_iterate(self._p)

    def sleepInterval(self):
        return tox_iteration_interval(self._p)

    def setName(self,name):
        logger.debug('Setting Name to: %s'%name)
        name = name.encode('utf-8')
        buffer = create_string_buffer(name, len(name))
        tox_self_set_name(self._p, buffer, len(buffer),None)


    def registerCallbacks(self):
        logger.debug('Register Callbacks')
        if(self._p != None):

            cb = tox_friend_request_cb(self.friend_request_callback)
            self._fRefs.append(cb)
            tox_callback_friend_request(self._p, cb,  py_object(self))

            cb = tox_friend_message_cb(self.friend_message_callback)
            self._fRefs.append(cb)
            tox_callback_friend_message(self._p, cb,  py_object(self))

            cb = tox_self_connection_status_cb(self.connection_status_callback)
            self._fRefs.append(cb)
            tox_callback_self_connection_status(self._p, cb, py_object(self))

            cb = tox_friend_connection_status_cb(self.friend_connection_status_callback)
            self._fRefs.append(cb)
            tox_callback_friend_connection_status(self._p, cb, py_object(self))

            cb = tox_friend_status_cb(self.friend_status_callback)
            self._fRefs.append(cb)
            tox_callback_friend_status(self._p, cb, py_object(self))

            cb = tox_friend_name_cb(self.friend_name_callback)
            self._fRefs.append(cb)
            tox_callback_friend_name(self._p, cb, py_object(self))

            cb = tox_file_recv_control_cb(self.file_recv_control_cb)
            self._fRefs.append(cb)
            tox_callback_file_recv_control(self._p, cb, py_object(self))

            cb = tox_file_recv_cb(self.file_recv_cb)
            self._fRefs.append(cb)
            tox_callback_file_recv(self._p, cb, py_object(self))

            cb = tox_file_recv_chunk_cb(self.file_recv_chunk_cb)
            self._fRefs.append(cb)
            tox_callback_file_recv_chunk(self._p, cb, py_object(self))

            cb = tox_file_chunk_request_cb(self.file_chunk_request_cb)
            self._fRefs.append(cb)
            tox_callback_file_chunk_request(self._p, cb, py_object(self))

            cb = tox_friend_lossless_packet_cb(self.friend_lossless_packet_callback)
            self._fRefs.append(cb)
            tox_callback_friend_lossless_packet(self._p, cb, py_object(self))

        else:
            logger.error("Self is None")


    def bootstrap(self,bootstrap_address,port,public_key):
        response = pointer(c_int(1))
        logger.debug("Bootstraping: " + str(public_key))
        ret = tox_bootstrap(self._p, bootstrap_address.encode('ascii') ,port , hex_to_buffer(public_key), response);
        if(response.contents.value != TOX_ERR_BOOTSTRAP_OK):
            logger.warning("Bootstrap  failed: " + str(response.contents.value))
        if(ret == False):
            logger.warning("Bootstrap failed")
        logger.debug("Bootstrap done")
        return ret

    @staticmethod
    def connection_status_callback(tox,connection_status,userdata):
        logger.debug("Connection Status Changed to: %s"%connection_status)
        logger.debug("Userdata: %s"%repr(userdata))
        self = cast(userdata, py_object).value
        self.on_connection_status(connection_status)

    def on_connection_status(self,connection_status):
        pass

    @staticmethod
    def friend_request_callback(tox, public_key, message, length, userdata):
        logger.debug("Got Friend request from: %s"%public_key)
        logger.debug("Message: %s"%message)
        self = cast(userdata, py_object).value
        self.on_friend_request(buffer_to_hex(public_key, TOX_PUBLIC_KEY_SIZE), ptr_to_string(message, length))

    @staticmethod
    def file_recv_control_cb(tox, friend_number, file_number, control, userdata):
        logger.debug("Got File Recieve Control Callback from: %s Number: %s"%(friend_number, file_number))
        self = cast(userdata, py_object).value
        self.on_file_recv_control(friend_number,file_number,control)

    @staticmethod
    def file_recv_cb(tox, friend_number, file_number, kind, file_size, filename, filename_length, userdata):
        logger.debug("Got File Recieve Callback from: %s Number: %s"%(friend_number, file_number))
        self = cast(userdata, py_object).value

        try:
            self.on_file_recv(friend_number,file_number,kind,file_size,ptr_to_string(filename, filename_length))
        except Exception as e:
            logger.debug("Error recieving file bla: " + str(e))

    @staticmethod
    def file_recv_chunk_cb(tox, friend_number, file_number, position, data, length, userdata):
        logger.debug("Got File Recieve Chunk Callback from: %s Number: %s Position: %s"%(friend_number, file_number, position))
        self = cast(userdata, py_object).value

        if(length==0):
            self.on_file_recv_chunk(friend_number,file_number,position,"")
            return

        try:
            self.on_file_recv_chunk(friend_number, file_number, position, ptr_to_buffer(data, length))
        except Exception as e:
            logger.debug("Error recieving file chunk: " + str(e))


    @staticmethod
    def file_chunk_request_cb(tox, friend_number, file_number, position, length, userdata):
        logger.debug("Got File Send Chunk Callback from: %s Number: %s Position: %s"%(friend_number, file_number, position))
        self = cast(userdata, py_object).value
        self.on_file_chunk_request(friend_number,file_number,position,length)


    def on_friend_request(self,public_key, message):
        pass

    def friend_add_norequest(self,address):
        logger.debug("Add Friend Norequest: %s"%address)
        ret = tox_friend_add_norequest(self._p,hex_to_buffer(address) ,None)
        if (ret == 4294967295):
            logger.error("Add Friend Norequest Failed: %s"%address)
            return -1

        logger.info("Added as FriendID: %s"%ret)
        return ret


    def friend_add(self,address,message):
        logger.debug('Add Friend: %s'%address)
        logger.debug('Message: %s'%message)
        message_send = None
        ret = None
        response = pointer(c_int(9))

        try:
            message_send = message.encode('utf-8')
        except:
            message_send = message

        try:
            #Is this Message correct???
            #~ logger.error("Tox init failed: " + str(response.contents.value))
            buffer = create_string_buffer(message_send, len(message_send))
            ret = int(tox_friend_add(self._p,hex_to_buffer(address),buffer,len(buffer) ,response))
        except Exception as e:
            logger.error("Friend add failed: " + str(e))
            return False

        if response.contents.value == TOX_ERR_FRIEND_ADD_OK:
            logger.info("Added as FriendID: %s"%ret)
            return True
        logger.error("friend_add failed: " + str(response.contents.value))
        return False


    def set_status(self, userstatus):
        logger.debug('Setting Status to: %s'%userstatus)
        tox_self_set_status(self._p,userstatus)

    def send_message(self,friend_id,message_type,message):
        logger.info('Sending Message to: %s Type: %s Length: %s'%(friend_id,message_type,len(message)))

        if message == None:
            logger.warning('No Message')
            return

        if(friend_id == None):
            logger.warning('No FriendID')
            return

        message_send = None
        try:
            message_send = message.encode('utf-8')
            logger.debug('Message encoded to UTF-8')
        except:
            message_send = message

        buffer = create_string_buffer(message_send, len(message_send))
        tox_friend_send_message(self._p,friend_id,message_type,buffer,len(buffer),None)
        logger.debug('Message Sended')


    def self_set_status_message(self,status):
        logger.debug('Setting Status Message to: %s'%status)
        buffer = create_string_buffer(status, len(status))
        return tox_self_set_status_message(self._p,buffer,len(buffer),None)


    @staticmethod
    def friend_message_callback(tox, friend_id, message_type, message, length, userdata):
        logger.info('Recieved Message from: %s type: %s length: %s'%(friend_id, message_type, length))
        self = cast(userdata, py_object).value
        self.on_friend_message(friend_id,message_type,ptr_to_string(message, length).decode('utf-8'))

    def on_friend_message(self,friend_id, message_type,message):
        pass


    def get_address(self):
        address = create_string_buffer(TOX_ADDRESS_SIZE)
        tox_self_get_address(self._p,address)
        hex_address = buffer_to_hex(address)
        logger.debug('Get own address: %s'%hex_address)
        return hex_address

    def get_public_key(self):
        public_key = create_string_buffer(TOX_PUBLIC_KEY_SIZE)
        tox_self_get_public_key(self._p,public_key)
        hex_public_key = buffer_to_hex(public_key)
        logger.debug('Get own Pubkey: %s'%hex_public_key)
        return hex_public_key


    @staticmethod
    def friend_connection_status_callback (tox,friendId,connection_status,userdata):
        logger.debug('Friend Connection (%s) changed to: %s'%(friendId,connection_status))
        self = cast(userdata, py_object).value
        self.on_friend_connection_status(friendId,connection_status)

    def on_friend_connection_status(self,friendId, connection_status):
        pass

    @staticmethod
    def friend_status_callback (tox,friendId,status,userdata):
        self = cast(userdata, py_object).value
        self.on_friend_connection_status(friendId,status)


    def on_friend_lossless_packet_callback(tox,friendId,message_type,message):
        pass

    @staticmethod
    def friend_lossless_packet_callback(tox,friendId,message,length,userdata):
        logger.debug('Recieved Lossless Packet from: %s length: %s'%(friendId,length))
        self = cast(userdata, py_object).value
        buffer = ptr_to_buffer(message, length)
        #first byte is message type
        message_type = ctypes.c_uint8()
        ctypes.memmove(addressof(message_type),buffer,1)
        self.on_friend_lossless_packet_callback(friendId,message_type.value,buffer[1:])

    def on_friend_status(self,friendId,status):
        pass

    def get_friend_list_size(self):
        size = tox_self_get_friend_list_size(self._p,None)
        logger.debug('Friend List Size: %s'%size)
        return size

    def get_friend_list(self):
        size = tox_self_get_friend_list_size(self._p)
        friendList = name_len_array = (c_uint32 * size)()
        tox_self_get_friend_list(self._p,friendList,None)
        logger.debug('Friend List: %s'%list(friendList))
        return friendList

    def friend_get_name_size(self,friendId):
        name_size = tox_friend_get_name_size(self._p,friendId,None)
        logger.debug('Get Name Size (%s): %s'%(friendId,size))
        return name_size

    def friend_get_public_key(self,friendId):
        public_key = create_string_buffer(TOX_PUBLIC_KEY_SIZE)
        tox_friend_get_public_key(self._p,friendId,public_key,None)
        hex_public_key = buffer_to_hex(public_key)
        logger.debug('Get Pubkey (%s): %s'%(friendId,hex_public_key))
        return hex_public_key
        

    def friend_get_name(self,friendId):
        size = tox_friend_get_name_size(self._p,friendId,None)
        buffer = create_string_buffer(size)
        tox_friend_get_name(self._p,friendId,buffer,None)
        dec_name = buffer.value.decode('utf-8')
        logger.debug('Get Name (%s): %s'%(friendId,dec_name))
        return dec_name


    def friend_exists(self,friendId):
        retval = tox_friend_exists(self._p,friendId)
        logger.debug('Friend exists (%s): %s'%retval)
        return retval

    def friend_delete(self,friendId):
        retval = tox_friend_delete(self._p,friendId,None)
        logger.info('Friend delete (%s): %s'%retval)
        return retval

    def self_get_name_size(self):
        size = tox_self_get_name_size(self._p,None)
        logger.debug('Get Own Name Size: %s'%(size))
        return size

    def self_get_name(self):
        size = tox_self_get_name_size(self._p,None)
        buffer = create_string_buffer(size)
        tox_self_get_name(self._p,buffer,None)
        dec_name = buffer.value.decode('utf-8')
        logger.debug('Get Own Name: %s'%dec_name)
        return dec_name

    @staticmethod
    def friend_name_callback(tox,friendId,name,length,userdata):
        self = cast(userdata, py_object).value
        name = ptr_to_string(name, length)
        logger.debug('Friend (%s) changed name to: %s'%(friendId,name))
        self.on_friend_name(friendId,name)

    def on_friend_name(self,friendId,name):
        pass

    def friend_get_status(self,friendId):
        status = tox_friend_get_status(self._p,friendId,None)
        logger.debug('Friend (%s) get status: %s'%(friendId,status))
        return status

    def friend_get_connection_status(self,friendId):
        status = tox_friend_get_connection_status(self._p,friendId,None)
        if (status == TOX_CONNECTION_NONE):
            logger.debug('Friend (%s) Not Connected'%friendId)
            return False
        logger.debug('Friend (%s) Connected'%friendId)
        return True


    def friend_get_status_message(self,friendId):
        size = tox_friend_get_status_message_size(self._p,friendId,None)
        buffer = create_string_buffer(size)
        tox_friend_get_status_message(self._p,friendId,buffer,None)
        dec_message = buffer.value.decode('utf-8')
        logger.debug('Friend (%s) Status Message: %s'%(friendId,dec_message))
        return dec_message

    def friend_get_typing(self,friendId):
        retval = tox_friend_get_typing ( self._p,friendId,None)
        logger.debug('Get Typing(%s): %s'%(friendId,retval))
        return retval

    def self_get_udp_port(self):
        retval = tox_self_get_udp_port (self._p,None)
        logger.debug('UDP Port: %s'%retval)
        return retval

    def self_get_tcp_port(self):
        retval = tox_self_get_tcp_port (self._p,None)
        logger.debug('TCP Port: %s'%retval)
        return retval

    def version_major(self):
        retval = tox_version_major()
        logger.debug('Major Version: %s'%retval)
        return retval

    def version_minor(self):
        retval = tox_version_minor()
        logger.debug('Minor Version: %s'%retval)
        return retval

    def version_patch(self):
        retval = tox_version_patch()
        logger.debug('Patch Version: %s'%retval)
        return retval

    def version_is_compatible(self,major,minor,patch):
        retval = tox_version_is_compatible (major, minor, patch )
        logger.debug('Version Compatible: %s'%retval)
        return retval

    def group_get_type(self,groupnumber):
        retval = tox_group_get_type (self._p,groupnumber)
        logger.debug('Group Type(%s): %s'%(groupnumber,retval))
        return retval

    def self_set_typing(self,friendId,is_typing):
        """Set typing needs a friendID?"""
        retval = tox_self_set_typing(self._p,friendId,is_typing,None)
        logger.debug('Set Typing(%s): %s'%(friendId,is_typing))
        return retval

    def kill(self):
        logger.info('Kill TOX')
        tox_kill(self._p)
        self._p = None
        logger.info('Done')

    def get_dht_id(self):
        dht_id = create_string_buffer(TOX_PUBLIC_KEY_SIZE)
        tox_self_get_dht_id (self._p,dht_id )
        hex_dht_id = buffer_to_hex(dth_id)
        logger.debug('DHT ID: %s'%hex_dht_id)
        return hex_dht_id

    def file_control(self,friend_number,file_number,control):
        return tox_file_control ( self._p,friend_number,file_number,control,None)

    def get_file_id(self,file_number):
        file_id = create_string_buffer(TOX_FILE_ID_LENGTH)
        tox_file_get_file_id ( self._p,friend_number,file_number,file_id,None)
        return file_id

    def file_seek(self,friend_number,file_number,position):
        return tox_file_seek (self._p,friend_number,file_number,position,None)


    def on_file_recv_control(self,friend_number, file_number,control):
        pass

    def on_file_recv_chunk(self,friend_number,file_number,position,data):
        pass

    def on_file_recv(self,friend_number,file_number,kind,file_size,filename):
        pass


    def on_file_chunk_request(self,friend_number,file_number,position,length):
        pass


    def hash_data(self,data):
        res_data = create_string_buffer(TOX_HASH_LENGTH)
        tox_hash (res_data, data,length(data))
        return res_data

    def file_send(self,friend_number,kind,file_size, file_id, filename):

        buffer = create_string_buffer(filename, len(filename))
        file_id_buffer = None
        if file_id:
            file_id_buffer = create_string_buffer(file_id, TOX_FILE_ID_LENGTH)

        return tox_file_send (self._p,friend_number,kind,file_size,file_id_buffer,buffer,len(buffer),None)


    def file_send_chunk(self,friend_number,file_number,position,data):
        data_buffer = create_string_buffer(data,len(data))
        tox_file_send_chunk (self._p,friend_number,file_number,position,data_buffer,len(data_buffer),None)


    def friend_send_lossless_packet(self,friend_number,message_type,data):
        response = pointer(c_int(TOX_ERR_FRIEND_CUSTOM_PACKET_OK))
        datalen = len(data)
        message_type = c_ubyte(message_type)
        buff = (c_ubyte * (datalen+1) )()

        ctypes.memmove(addressof(buff),addressof(message_type),ctypes.sizeof(message_type))
        ctypes.memmove(addressof(buff)+1,addressof(data),ctypes.sizeof(data))

        tox_friend_send_lossless_packet(self._p,friend_number,buff,len(buff),response)
        if ( response.contents.value == TOX_ERR_FRIEND_CUSTOM_PACKET_OK):
            logger.debug("Lossless package sent: " + str(response.contents.value))
            return True

        logger.debug("Lossless package failed: " + str(response.contents.value))
        return False


    def friend_send_lossy_packet(self,friend_number,data):
        data_buffer = create_string_buffer(data,len(data))
        return tox_friend_send_lossy_packet(self._p,friend_number,data_buffer,len(data_buffer),None)


    def self_get_connection_status(self):
        return tox_self_get_connection_status(self._p) != TOX_CONNECTION_NONE



    #uint32_t tox_get_chatlist  (   const Tox *     tox,
    #       int32_t *   out_list,
    #       uint32_t    list_size
    #   )



    #int tox_group_get_names    (   const Tox *     tox,
    #       int     groupnumber,
    #       uint8_t     names[][TOX_MAX_NAME_LENGTH],
    #       uint16_t    lengths[],
    #       uint16_t    length
    #   )




    #void   tox_options_default (struct Tox_Options *options)

    #struct Tox_Options *   tox_options_new (TOX_ERR_OPTIONS_NEW *error)

    #void   tox_options_free (struct Tox_Options *options)







