class ChatDisptcher(object):

	def __init__(self, connection):
		self.connection = connection
		self.handles = {
			opcode.REQ_ENTER_ROOM : self.enter_room,
			opcode.REQ_LEAVE_ROOM : self.leave_room,
			opcode.REQ_ROOM_MSG : self.room_msg
		}

	def __call__(self, netpacket):
		handle = self.handles.get(netpacket.opcode, self.handle_unkonw)
		handle(netpacket)

	def enter_room(self, netpacket):
		LOGGER.info('enter_room')
		room_name = netpacket.data
		sRoomMgr.add_peer_to_room(room_name, self.connection.peer)
		self.send(opcode.REQ_ENTER_ROOM, 'enter room')
		
	def leave_room(self, netpacket):
		room_name = netpacket.data
		LOGGER.info('leave_room')
		sRoomMgr.remove_peer_from_room(room_name, self.connection.peer)
		self.send(opcode.REQ_LEAVE_ROOM, 'leave room')

	def room_msg(self, netpacket):
		LOGGER.info('room_msg')
		data = netpacket.to_json()
		msg = Message(data['payload'], self.connection.peer)
		sRoomMgr.broadcast(data['room_name'], msg)

	def handle_unkonw(self, netpacket):
		self.send(opcode.REQ_NONE, 'unkow packet opcode')

	def send(self, code, message):
		self.connection.send(code, message)