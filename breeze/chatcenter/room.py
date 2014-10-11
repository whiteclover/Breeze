class Room(object):

	def __init__(self, name):
		self.name
		self.peers = {}
		self.messages = []
		self.message_limit = 1000
		self.peer_limit = 100
		self.in_pos = 0
		self.out_pos = 0

	def add_message(self, message):
		if self.in_pos != self.out_pos:
			self.messages[self.in_pos+1] = messages

	def add_peer(self, peer):
		if peer.uid in self.peers:
			raise Exception('in')
		self.peers[peer.uid] = peer

	def remove_peer(self, peer):
		del self.peers[peer.uid]


