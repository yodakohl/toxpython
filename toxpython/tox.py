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
				print("Error loading savedata: " +str(e) )


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
		#	if k not in options:
		#		options[k] = v
		opt.ipv6_enabled = c_bool(True)
		opt.udp_enabled = c_bool(True)
		opt.proxy_type = TOX_PROXY_TYPE_NONE
		opt.proxy_host = String(None)
		opt.proxy_port =0
		opt.start_port = 0
		opt.end_port =0

		if(mbuffer != None):
			opt.savedata_type = TOX_SAVEDATA_TYPE_TOX_SAVE
			opt.savedata_data = pointer(mbuffer)
			opt.savedata_length = datalen
		else:
			opt.savedata_type = TOX_SAVEDATA_TYPE_NONE

		response = pointer(c_int(9))
		self._p = tox_new(pointer(opt),response)

		if response.contents.value != TOX_ERR_NEW_OK:
			print("Tox init failed: " + str(response.contents.value))
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

		else:
			print("Self is None")


	def bootstrap(self,bootstrap_address,port,public_key):
		response = pointer(c_int(1))
		print("Bootstraping: " + str(public_key))
		ret = tox_bootstrap(self._p, bootstrap_address.encode('ascii') ,port , hex_to_buffer(public_key), response);
		if(response.contents.value != TOX_ERR_BOOTSTRAP_OK):
			print("Bootstrap  failed: " + str(response.contents.value))
		if(ret == False):
			print("Bootstrap failed")
		print("Bootstrap done")
		return ret

	@staticmethod
	def connection_status_callback(tox,connection_status,userdata):
		print("connection_status_callback")
		self = cast(userdata, py_object).value
		self.on_connection_status(connection_status)

	def on_connection_status(self,connection_status):
		pass

	@staticmethod
	def friend_request_callback(tox, public_key, message, length, userdata):
		self = cast(userdata, py_object).value
		self.on_friend_request(buffer_to_hex(public_key, TOX_PUBLIC_KEY_SIZE), ptr_to_string(message, length))

	@staticmethod
	def file_recv_control_cb(tox, friend_number, file_number, control, userdata):
		self = cast(userdata, py_object).value
		self.on_file_recv_control(friend_number,file_number,control)

	@staticmethod
	def file_recv_cb(tox, friend_number, file_number, kind, file_size, filename, filename_length,userdata):
		self = cast(userdata, py_object).value

		try:
			self.on_file_recv(friend_number,file_number,kind,file_size,ptr_to_string(filename, filename_length))
		except Exception as e:
			print("Error recieving file bla: " + str(e))

	@staticmethod
	def file_recv_chunk_cb(tox, friend_number, file_number, position, data, length,userdata):
		self = cast(userdata, py_object).value

		if(length==0):
			self.on_file_recv_chunk(friend_number,file_number,position,"")
			return 
		
		try:
			self.on_file_recv_chunk(friend_number,file_number,position,ptr_to_buffer(data,length))
		except Exception as e:
			print("Error recieving file chunk: " + str(e))


	@staticmethod
	def file_chunk_request_cb(tox, friend_number, file_number, position, length,userdata):
		self = cast(userdata, py_object).value
		self.on_file_chunk_request(friend_number,file_number,position,length)




	def on_friend_request(self,public_key, message):
		pass

	def friend_add_norequest(self,address):
		ret = tox_friend_add_norequest(self._p,hex_to_buffer(address) ,None)
		if (ret == 4294967295):
			return -1

		return ret


	def friend_add(self,address,message):

		message_send = None
		ret = None
		response = pointer(c_int(9))

		try:
			message_send = message.encode('utf-8')
		except: 
			message_send = message
			
		try:


			print("Tox init failed: " + str(response.contents.value))
			buffer = create_string_buffer(message_send, len(message_send))
			ret = int(tox_friend_add(self._p,hex_to_buffer(address),buffer,len(buffer) ,response))
		except Exception as e:
			print("Friend add failed: " + str(e)) 
			return False

		if response.contents.value == TOX_ERR_FRIEND_ADD_OK:
			return True
                print("friend_add failed: " + str(response.contents.value))
		return False


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def set_status(self, userstatus):
		tox_self_set_status(self._p,userstatus)


	def send_message(self,friend_id,message_type,message):
		if message == None:
			return

		if(friend_id == None):
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
		self.on_friend_message(friend_id,message_type,ptr_to_string(message, length).decode('utf-8'))

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

	def get_friend_list(self):
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


	def friend_send_lossless_packet(self,friend_number,data):
		data_buffer = create_string_buffer(data,len(data))
		return tox_friend_send_lossless_packet(self._p,friend_number,data_buffer,len(data_buffer))


	def friend_send_lossy_packet(self,friend_number,data):
		data_buffer = create_string_buffer(data,len(data))
		return tox_friend_send_lossy_packet(self._p,friend_number,data_buffer,len(data_buffer))


	def self_get_connection_status(self):
		return tox_self_get_connection_status(self._p) != TOX_CONNECTION_NONE



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




	#void 	tox_options_default (struct Tox_Options *options)
	 
	#struct Tox_Options * 	tox_options_new (TOX_ERR_OPTIONS_NEW *error)
	 
	#void 	tox_options_free (struct Tox_Options *options)







