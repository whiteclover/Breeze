

class NetPacket(object):
	MAX_LEN = 2**16
	def __init__(self, stream, addr):
		self.stream = stream
		self.addr = addr

