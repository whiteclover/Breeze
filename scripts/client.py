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
		for i in range(10):
			if i == 0:
				send(client, opcode.REQ_PING, 'ping')
				recv(client)
			else:
				send(client, opcode.REQ_ROOM_MSG, 'room msg')
		time.sleep(5)
		for i in range(100):
			recv(client)
	except KeyboardInterrupt:
			exit(1)