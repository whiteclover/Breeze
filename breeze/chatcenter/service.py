import logging
from tornado.tcpserver import TCPServer
from tornado.iostream import IOStream
import tornado.ioloop
import time
import struct

from breeze.chatcenter.peer import Peer
from breeze.chatcenter.message import Message
from breeze.chatcenter.room import Room
from breeze.net.heartbeat import HeartBeat
from breeze.net.netpacket import NetPacket
from breeze.chatcenter import opcode

LOGGER = logging.getLogger(__name__)

ROOM = Room('test')
sHeartBeatMgr = HeartBeat()


class ChatConnection(object):

	_SEED = 0

	def __init__(self, stream, addr, net_handler=None):
		LOGGER.info('conn stream : %s', stream)
		self.stream = stream
		self.addr = addr
		self.authed = False
		LOGGER.info("SEED : %d", self._SEED)
		ChatConnection._SEED = ChatConnection._SEED + 1
		self.packet = NetPacket(opcode.REQ_NONE, '', 0)
		self.net_handler = net_handler
		self.peer = Peer(self, str(ChatConnection._SEED))
		ROOM.add_peer(self.peer)
		self.stream.set_close_callback(self.on_connection_close)
		self.on_conneted()

	def on_conneted(self):
		sHeartBeatMgr.update(self)
		self.stream.read_bytes(2, self.on_head)

	def on_connection_close(self):
		self.close()

	def close(self):
		if self.stream:
			LOGGER.info('close stream:%s', self.stream)
			self.stream.close()
		LOGGER.info('call close')
		ROOM.remove_peer(self.peer)
		sHeartBeatMgr.remove(self)


	def on_head(self, data):
		cmd, leng  = struct.unpack("!BB", data)
		self.packet.opcode = cmd
		self.packet.size = leng
		self.stream.read_bytes(leng, self.on_body)

	def on_body(self, data):
		self.packet.data = data
		self.handle_packet()
		self.stream.set_nodelay(False)
		self.on_conneted()

	def handle_packet(self):
		if self.packet.opcode == opcode.REQ_PING:
			msg = Message('PONG', self.peer)
			self.write_reply(opcode.REQ_PING, msg)
		elif self.packet.opcode == opcode.REQ_ROOM_MSG:
			LOGGER.info('ROOM MSG')
			msg = Message('nihao', self.peer)
			ROOM.broadcast(msg)
		else:
			if self.net_handler:
				self.netpacket(self, handle_packet)

	def write_reply(self, code, msg):
		LOGGER.info('msg : %s', msg.msg)
		head = struct.pack('!BB', code, len(msg.msg))
		head += msg.msg
		self.stream.write(head)


	def handle_ping(self, netpacket):
		pass

	def handle_login(self, netpacket):
		pass

	def handle_logoff(self, netpacket):
		pass

	def handle_kick(self, netpacket):
		pass

	def handle_enter_room(self, netpacket):
		pass

	def handle_leave_room(self, netpacket):
		pass

	def handle_sub_channel(self, netpacket):
		pass


	def handle_unsub_channel(self, netpacket):
		pass

	def handle_enter_guild(self, netpacket):
		pass


	def handle_leave_guild(self, netpacket):
		pass

	def handle_add_friend_req(self, netpacket):
		pass

	def handle_remove_friend(self, netpacket):
		pass


	def handle_kick(self, netpacket):
		pass




class ChatServer(TCPServer):
	"""docstring for ChatServer"""
	def __init__(self, io_loop=None, timeout_secs=10, **kwargs):
		io_loop = io_loop or tornado.ioloop.IOLoop.current()
		self.timeout_secs = 10
		sHeartBeatMgr.initialize(io_loop, timeout_secs)
		sHeartBeatMgr.heartbeat()
		#sRoomMgr.heartbeat()
		TCPServer.__init__(self, io_loop=io_loop, **kwargs)

	def handle_stream(self, stream, address):
		ChatConnection(stream, address)

	def _handle_connection(self, connection, address):
		try:
			stream = IOStream(connection, io_loop=self.io_loop, max_buffer_size=self.max_buffer_size)
			self.handle_stream(stream, address)
		except Exception:
			LOGGER.error("Error in connection callback", exc_info=True)



class ChatService(object):
	def __init__(self):
		self.server = ChatServer()

	def start(self):
		try:
			self.server.bind(8011, address='127.0.0.1', backlog=1024)
			self.server.start()
			tornado.ioloop.IOLoop.instance().start()
		except KeyboardInterrupt:
			tornado.ioloop.IOLoop.instance().stop()