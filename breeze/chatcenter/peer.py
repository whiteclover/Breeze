class Peer(object):

	def __init__(self, name):
		self.uid = uid
		self.name = name
		self.in_room = []
		self.in_guild = []
		self.in_channel = []
		self.token = token


	def __eq__(self, other_peer):
		return self.uid == other_peer.uid
	
	def send(self, msg):
		self.sock.write(msg)