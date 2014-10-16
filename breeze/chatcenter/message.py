import time

class Message(object):

    def __init__(self, msg, user):
    	self.user = user
        self.create_at = time.time()
        self.msg = msg
