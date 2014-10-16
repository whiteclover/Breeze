from breeze.chatcenter.service import ChatService
import logging

debug = True
level = logging.DEBUG if debug else logging.INFO
logging.basicConfig(level=level,
	format='%(asctime)s %(levelname)-8s %(message)s',
	datefmt='%Y-%m-%d %H:%M:%S', filemode='a+')

if __name__ == '__main__':
	ChatService().start()