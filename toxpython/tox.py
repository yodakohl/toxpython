import datetime
import time

from .ctox import *
from .util import *

## Todo: Proper error handling
## Todo: Implement missing API


class ToxAV():

	_p = None


	def init(self,ToxInstance):

		self._p = toxav_new (ToxInstance, 100) #max calls = 100


class Tox():

	_p = None

	_fRefs = []

	def init(self,fileName=None, options=None):

		buffer = None
		datalen = 0
		if( fileName != None):
			try:
				with open(fileName, 'rb') as f:
					userdata = f.read()
					datalen = len(userdata)
					buffer = create_string_buffer(userdata, len(userdata))
			except:
				pass

		defaults = {
			'ipv6_enabled': True,
			'udp_disabled': False,
			'proxy_type': TOX_PROXY_TYPE_NONE,
			'proxy_host': '',
			'proxy_port': 0,
			'start_port': 0,
			'end_port': 10000,
		}

		if(options == None):
			options = defaults

		for k, v in defaults.items():
			if k not in options:
				options[k] = v
				opt = Tox_Options()
				opt.ipv6_enabled = c_bool(options['ipv6_enabled'])
				opt.udp_disabled = c_bool(options['udp_disabled'])
				opt.proxy_host = options['proxy_host'][:255].encode('ascii') + b'\0'
				opt.proxy_port = c_uint16(options['proxy_port'])
				opt.start_port = c_uint16(options['start_port'])
				opt.end_port = c_uint16(options['end_port'])
				#self._p = tox_new(cast(pointer(opt), c_void_p),None,0,None)
		self._p = tox_new(None,buffer,datalen,None)

		self.registerCallbacks()



	def save(self,fileName):
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
		name = name.encode('utf-8')
		buffer = create_string_buffer(name, len(name))
		tox_self_set_name(self._p, buffer, len(buffer),None)


	def registerCallbacks(self):
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


		else:
			print("Self is None")


	def bootstrap(self,bootstrap_address,port,public_key):
		return tox_bootstrap(self._p, bootstrap_address.encode('ascii') ,port , hex_to_buffer(public_key), None);

	@staticmethod
	def connection_status_callback(tox,connection_status,userdata):
		self = cast(userdata, py_object).value
		self.on_connection_status(connection_status)

	def on_connection_status(self,connection_status):
		pass

	@staticmethod
	def friend_request_callback(tox, public_key, message, length, userdata):
		self = cast(userdata, py_object).value
		self.on_friend_request(buffer_to_hex(public_key, TOX_PUBLIC_KEY_SIZE), ptr_to_string(message, length))

	def on_friend_request(self,public_key, message):
		pass

	def add_friend_norequest(self,address):
		ret = tox_friend_add_norequest(self._p,hex_to_buffer(address) ,None)
		if (ret == 4294967295):
			return -1

		return ret


	#untested
	def friend_add(self,address,message):

		message_send = None
		try:
			message_send = message.encode('utf-8')
		except: 
			message_send = message

		buffer = create_string_buffer(message_send, len(message_send))
		ret = int(tox_friend_add(self._p,hex_to_buffer(address),buffer,len(buffer) ,None))
		#print(str(ret))
		#if (ret == 4294967295):
		#	return -1

		return ret


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def send_message(self,friend_id,message_type,message):
		if message == None:
			return 

		message_send = None
		try:
			message_send = message.encode('utf-8')
		except: 
			message_send = message

		buffer = create_string_buffer(message_send, len(message_send))
		tox_friend_send_message(self._p,friend_id,message_type,buffer,len(buffer),None)


	def self_set_status_message(self,status):
		buffer = create_string_buffer(status, len(status))
		return tox_self_set_status_message(self._p,buffer,len(buffer),None)


	@staticmethod
	def friend_message_callback(tox, friend_id,message_type, message, length, userdata):
		self = cast(userdata, py_object).value
		self.on_friend_message(friend_id,message_type, ptr_to_string(message, length))

	def on_friend_message(self,friend_id, message_type,message):
		pass


	def get_address(self):
		address = create_string_buffer(TOX_ADDRESS_SIZE)
		tox_self_get_address(self._p,address)
		return buffer_to_hex(address)

	def get_public_key(self):
		public_key = create_string_buffer(TOX_PUBLIC_KEY_SIZE)
		tox_self_get_public_key(self._p,public_key)
		return buffer_to_hex(public_key)


	@staticmethod
	def friend_connection_status_callback (tox,friendId,connection_status,userdata):
		self = cast(userdata, py_object).value
		self.on_friend_connection_status(friendId,connection_status)

	def on_friend_connection_status(self,friendId, connection_status):
		pass


	@staticmethod
	def friend_status_callback (tox,friendId,status,userdata):
		self = cast(userdata, py_object).value
		self.on_friend_connection_status(friendId,status)

	def on_friend_status(self,friendId,status):
		pass

	def get_friend_list_size(self):
		return tox_self_get_friend_list_size(self._p,None)

	def getFriendList(self):
		size = tox_self_get_friend_list_size(self._p)
		friendList = name_len_array = (c_uint32 * size)()
		tox_self_get_friend_list(self._p,friendList,None)
		return friendList

	def friend_get_name_size(self,friendId):
		return tox_friend_get_name_size(self._p,friendId,None)

	def friend_get_name(self,friendId):
		size = tox_friend_get_name_size(self._p,friendId,None)
		buffer = create_string_buffer(size)
		tox_friend_get_name(self._p,friendId,buffer,None)
		return buffer.value.decode('utf-8')


	def friend_exists(self,friendId):
		return tox_friend_exists(self._p,friendId)

	def friend_delete(self,friendId):
		return tox_friend_delete(self._p,friendId,None)

	def self_get_name_size(self):
		return tox_self_get_name_size(self._p,None)

	def self_get_name(self):
		size = tox_self_get_name_size(self._p,None)
		buffer = create_string_buffer(size)
		tox_self_get_name(self._p,buffer,None)
		return buffer.value.decode('utf-8')


	@staticmethod
	def friend_name_callback(tox,friendId,name,length,userdata):
		self = cast(userdata, py_object).value
		self.on_friend_name(friendId,ptr_to_string(name, length))

	def on_friend_name(self,friendId,name):
		pass

	def friend_get_status(self,friendId):
		status = tox_friend_get_status(self._p,friendId)
		return status

	def friend_get_connection_status(self,friendId):
		status = tox_friend_get_connection_status(self._p,friendId,None)
		if (status == TOX_CONNECTION_NONE):
			return False
		return True


	def friend_get_status_message(self,friendId):
		size = tox_friend_get_status_message_size(self._p,friendId,None)
		buffer = create_string_buffer(size)
		tox_friend_get_status_message(self._p,friendId,buffer,None)
		return buffer.value.decode('utf-8')

	#def group_get_title(self,groupnumber):
	#	buffer = create_string_buffer(size)
	#	return tox_group_get_title (self._p,groupnumber,uint8_t * title,uint32_t max_length )


	def friend_get_status_message(self,friendId):
		return tox_friend_get_status_message_size(self._p,friendId,None)


	def friend_get_typing(self,friendId):
		return tox_friend_get_typing ( self._p,friendId,None)

	def self_get_udp_port(self):
		return tox_self_get_udp_port (self._p,None)

	def self_get_tcp_port(self):
		return tox_self_get_tcp_port (self._p,None)

	def version_major(self):
		return tox_version_major()

	def version_minor(self):
		return tox_version_minor()

	def version_patch(self):
		return tox_version_patch()

	def version_is_compatible(self,major,minor,patch):
		return tox_version_is_compatible (major, minor, patch )


	def group_get_type(self,groupnumber):
		return tox_group_get_type (self._p,groupnumber)

	def self_set_typing(self,friendId,is_typing):
		return tox_self_set_typing(self._p,friendId,is_typing,None)


	def kill(self):
		tox_kill(self._p)
		self._p = None

	def get_dht_id(self):
		dht_id = create_string_buffer(TOX_PUBLIC_KEY_SIZE)
		tox_self_get_dht_id (self._p,dht_id )
		return buffer_to_hex(dth_id)


#To test
#	def file_control(self):
#		return tox_file_control ( self._p,friend_number,file_number,control,None) 

#	def get_file_id(self):
#		tox_file_get_file_id ( self._p,friend_number,file_number,file_id,None)

#	def file_seek(self):
#		bool tox_file_seek (self._p,friend_number,file_number,position,None)


#	def file_send():
#		tox_file_send (self._p,uint32_t friend_number,uint32_t kind,uint64_t file_size,const uint8_t * file_id,const uint8_t * filename,size_t filename_length,None)


#	def file_send_chunk():
#		bool tox_file_send_chunk (self._p, uint32_t friend_number,uint32_t file_number,uint64_t position,const uint8_t * data,size_t length,None)


#bool tox_friend_send_lossless_packet 	( 	Tox *  	tox,
#		uint32_t  	friend_number,
#		const uint8_t *  	data,
#		size_t  	length,
#		TOX_ERR_FRIEND_CUSTOM_PACKET *  	error 
#	)

#bool tox_friend_send_lossy_packet 	( 	Tox *  	tox,
#		uint32_t  	friend_number,
#		const uint8_t *  	data,
#		size_t  	length,
#		TOX_ERR_FRIEND_CUSTOM_PACKET *  	error 
#	) 	


#uint32_t tox_get_chatlist 	( 	const Tox *  	tox,
#		int32_t *  	out_list,
#		uint32_t  	list_size 
#	) 	



#int tox_group_get_names 	( 	const Tox *  	tox,
#		int  	groupnumber,
#		uint8_t  	names[][TOX_MAX_NAME_LENGTH],
#		uint16_t  	lengths[],
#		uint16_t  	length 
#	) 	










