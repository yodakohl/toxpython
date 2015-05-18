
import os
from toxpython import TOX_MESSAGE_TYPE_NORMAL
from toxpython import TOX_FILE_CONTROL_RESUME

class FileTransfer():
	filePointer = None
	filePath = ""
	callback = None

	def __init__(self):
		pass


class FiletransferList():

	client = None
	friendDicts={}

	def __init__(self,toxinstance):
		self.client = toxinstance

	def file_chunk_request(self,friend_number,file_number,position,length):
		print("File Chunk Request:" + str(position) + " " + str(length))
		transfer = self.friendDicts[friend_number][file_number]
		cur_pos = transfer.filePointer.tell()
		if not cur_pos == position:
			print("seeking position")
			transfer.filePointer.seek(position, 0)
		data = transfer.filePointer.read(length)
		self.client.file_send_chunk(friend_number,file_number,position,data)
		print("Chunk sent")

	def file_recv_control(self,friend_number, file_number,control):
		print("On file control recv")
		pass

	#Todo: check position
	def file_recv_chunk(self,friend_number,file_number,position,data):
		transfer = self.friendDicts[friend_number][file_number]
		
		if (len(data) == 0):
			transfer.filePointer.close()
			self.friendDicts[friend_number][file_number] = None
			transfer.callback(True)
			#Maby callback for file transfer finished
		else:
			transfer.filePointer.write(data)

	def recieveFile(self,friend_number,file_number,filename,size,callback):
		self.client.file_control(friend_number,file_number,TOX_FILE_CONTROL_RESUME)
		
		if friend_number not in self.friendDicts:
			self.friendDicts[friend_number] = {}

		fileptr = open(filename,"wb")

		transfer = FileTransfer()
		transfer.filePointer = fileptr
		transfer.filePath = filename
		transfer.callback = callback

		self.friendDicts[friend_number][file_number] = transfer


	#Send file, true if successfull
	def addFileTransfer(self,friend_number,filename):

		#file does not exist
		if not os.path.isfile(filename):
			return false 

		file_size = os.path.getsize(filename)
 		file_id = self.client.file_send(friend_number,TOX_MESSAGE_TYPE_NORMAL,file_size, None, filename)

		if friend_number not in self.friendDicts:
			self.friendDicts[friend_number] = {}

		fileptr = open(filename,"rb")

		transfer = FileTransfer()
		transfer.filePointer = fileptr
		transfer.filePath = filename

		self.friendDicts[friend_number][file_id] = transfer













