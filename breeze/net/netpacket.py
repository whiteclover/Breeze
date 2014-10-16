from breeze.util import json_loads

class NetPacket(object):
	def __init__(self, opcode, data='', data_len=0):
		self.opcode = opcode
		self.data = data
		self.size = data_len

	def to_json(self):
		return json_loads(self.data)