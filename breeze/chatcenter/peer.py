class Peer(object):

	def __init__(self, con, uid=None, name=None, token=None):
		self.uid = uid
		self.name = name
		self.in_room = {}
		self.in_guild = []
		self.in_channel = []
		self.token = token
		self.con  = con

	def __eq__(self, other_peer):
		return self.uid == other_peer.uid

	def add_room(self, room):
		self.in_room[room.name] = room
		
	def remove_room(self, room):
		del self.in_room[room.name]
	
	def send(self, msg):
		self.con.write_reply(2, msg)

	def clear(self):
		for room in self.in_room.values():
			room.remove_peer(self)

class AccountManager(object):

	def __init__(self):
		self.peers = {}

	def add(self, sid, peer):
		self.peers[sid] = peer

	def find(self, sid):
		return self.peers.get(sid)

	def update(self, sid, peer):
		if sid in self.peers:
			self.peers[sid] = peer

	def remove(self, sid, peer):
		if sid in self.peers():
			del self.peers[sid]

	def __contains__(self, sid):
		return self.sid in self.peers