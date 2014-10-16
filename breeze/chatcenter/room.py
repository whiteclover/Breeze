import time

class Room(object):

	def __init__(self, name):
		self.name = name
		self.peers = {}

	def broadcast(self, msg):
		if msg:
			for peer in self.peers.values():
				if peer != msg.user:
					peer.send(msg)

	def add_peer(self, peer):
		if peer.uid in self.peers:
			raise Exception('in')
		peer.add_room(self)
		self.peers[peer.uid] = peer

	def remove_peer(self, peer):
		peer.remove_room(self)
		del self.peers[peer.uid]


class RoomManager(object):

	def __init__(self):
		self.rooms = {}

	def add_room(self, room):
		self.rooms[room.name] = room

	def remove_room(self, room):
		if room.name in self.rooms:
			del self.rooms[room.name]

	def broadcast(self, room_name, msg):
		room = self.rooms.get(room_name)
		if room:
			room.broadcast(msg)