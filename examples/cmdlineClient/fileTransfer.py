
import os
from toxpython import TOX_MESSAGE_TYPE_NORMAL


class FileTransfer():
	filePointer = None
	filePath = ""

	def __init__(self):
		pass


class FiletransferList():

	client = None
	friendDicts={}


	def __init__(self,toxinstance):
		self.client = toxinstance


	def file_chunk_request(self,friend_number,file_number,position,length):
		transfer = self.friendDicts[friend_number][file_number]
		cur_pos = transfer.filePointer.tell()
		if not cur_pos == position:
			transfer.filePointer.seek(position, 0)
		data = transfer.filePointer.read(length)
		self.client.file_send_chunk(friend_number,file_number,position,data)


	#Send file, true if successfull
	def addFileTransfer(self,userid,filename):

		#file does not exist
		if not os.path.isfile(filename):
			return false 

		file_size = os.path.getsize(filename)
 		file_id = self.client.file_send(userid,TOX_MESSAGE_TYPE_NORMAL,file_size, None, filename)

		if userid not in self.friendDicts:
			self.friendDicts[userid] = {}

		fileptr = open(filename,"rb")

		transfer = FileTransfer()
		transfer.filePointer = fileptr
		transfer.filePath = filename

		self.friendDicts[userid][file_id] = transfer













