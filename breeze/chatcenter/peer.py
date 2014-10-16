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