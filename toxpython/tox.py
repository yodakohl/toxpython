import datetime
import time

from .ctox import *
from .util import *

## Todo: Proper error handling
## Todo: Implement missing API

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
	def add_friend(self,address,message):
		buffer = create_string_buffer(message_send, len(message))
		ret = tox_friend_add(self._p,hex_to_buffer(address),buffer,len(buffer) ,None)
		if (ret == 4294967295):
			return -1

		return ret


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def send_message(self,friend_id,message_type,message):
		message_send = None
		try:
			message_send = message.encode('utf-8')
		except: 
			message_send = message

		buffer = create_string_buffer(message_send, len(message_send))
		tox_friend_send_message(self._p,friend_id,message_type,buffer,len(buffer),None)

	@staticmethod
	def friend_message_callback(tox, friend_id,message_type, message, length, userdata):
		self = cast(userdata, py_object).value
		self.on_friend_message(friend_id,message_type, ptr_to_string(message, length))

	def on_friend_message(self,friend_id, message_type,message):
		pass

	def friend_add(self,address, message):
		message = message.encode('utf-8')
		buffer = create_string_buffer(message, len(message))
		address = hex_to_buffer(address)
		tox_friend_add(self._p,address,buffer,len(buffer),None)

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
		return tox_self_get_friend_list_size(self._p)

	def getFriendList(self):
		size = tox_self_get_friend_list_size(self._p)
		friendList = name_len_array = (c_uint16 * size)()
		tox_self_get_friend_list(self._p,friendList)
		return friendList

#tox_friend_get_name_size
#tox_friend_get_name
#tox_friend_get_status
#tox_friend_get_connection_status 



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









