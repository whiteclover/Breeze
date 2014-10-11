class Message(object):

    def __init__(self, msg):
        self._id = uuid()
        self.create_at = time.time()
        self.msg = msg
