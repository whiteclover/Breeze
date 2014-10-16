import time

class HeartBeat(object):

	def __init__(self):
		self.conns = {}
		self.io_loop = None

	def initialize(self, io_loop, timeout_secs=10):
		self.timeout_secs = timeout_secs
		self.io_loop = io_loop

	def add(self, conn):
		self.conns[conn] = time.time()

	def update(self, conn):
		self.conns[conn] = time.time()

	def remove(self, conn):
		if conn in self.conns:
			del self.conns[conn]

	def heartbeat(self):
		self.io_loop.add_timeout(time.time() + self.timeout_secs, self._heartbeat)

	def _heartbeat(self):	
		if self.conns:
			conns = self.conns.keys()
			for conn in conns:
				if (time.time() - self.conns[conn])  > self.timeout_secs:
					conn.close()
		self.heartbeat()