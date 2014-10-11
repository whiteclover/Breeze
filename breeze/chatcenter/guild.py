class Guild(object):

	def __init__(self):
		self.peers = {}
		self.message = []

	def broadcast(self):
		msg = self.message.pop(0)
		for peer in self.peers:
			peer.send(msg)

	def add_msg(self, msg):
		self.message.append(msg)

	def remove_peer(self, peer):
		del self.peers[peer_id]
		self.add_msg('leave peer')

	def add_peer(self, peer):
		self.peers[peers.uid] = peer
		self.add_msg('enter peer')