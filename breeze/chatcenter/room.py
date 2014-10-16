import time
import logging

LOGGER = logging.getLogger(__name__)
class Room(object):

	def __init__(self, name):
		self.name = name
		self.peers = {}

	def broadcast(self, msg):
		if msg:
			for peer in self.peers.values():
				if peer != msg.user:
					LOGGER.info('peer: %s', peer)
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

	def add_peer_to_room(self, room_name, peer):
		room = self.rooms.get(room_name)
		if not room:
			room = Room(room_name)
			self.rooms[room_name] = room
		room.add_peer(peer)

	def remove_peer_from_room(self, room_name, peer):
		room = self.rooms.get(room_name)
		if room:
			room.remove_peer(peer)

	def broadcast(self, room_name, msg):
		room = self.rooms.get(room_name)
		if room:
			room.broadcast(msg)
