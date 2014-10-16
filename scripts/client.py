import socket
import logging
import struct
import time
logger = logging.getLogger('client')

from breeze.chatcenter import opcode

def send(client, code, msg):
	head = struct.pack('!BB', code, len(msg))
	client.sendall(head+msg)

def recv(client):
		data = client.recv(2)
		cmd, leng  = struct.unpack("!BB", data)
		data = client.recv(leng)
		print 'cmd : %d, msg : %s' %(cmd, data)


if __name__ == '__main__':
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.connect(('127.0.0.1', 8011))

	try:
		send(client, opcode.REQ_PING, 'ping')
		recv(client)
		send(client, opcode.REQ_ENTER_ROOM, 'test_room')
		recv(client)
		time.sleep(5)
		print 'recv room msg'
		for i in range(100):
			recv(client)
		send(client, opcode.REQ_LEAVE_ROOM, 'test_room')
		recv(client)
		client.close()
	except KeyboardInterrupt:
			exit(1)