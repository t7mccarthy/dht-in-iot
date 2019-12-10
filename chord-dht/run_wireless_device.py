import asyncio
import sys

from chord import *
from iot_sim_chord import *

import math
import random
import time

def nextTime(rateParameter = 1/1):
    return -math.log(1.0 - random.random()) / rateParameter

loop = asyncio.get_event_loop()
# proxy = ClientNode(Address("127.0.0.1", 3001 + int(sys.argv[1])))#, Address("127.0.0.1", 3500 + int(sys.argv[1])))
server = Node(Address("127.0.0.1", 3001 + int(sys.argv[1])), Address("127.0.0.1", 3000))
# proxy = ClientNode(Address("127.0.0.1", 3001 + int(sys.argv[1])))#, Address("127.0.0.1", 3500 + int(sys.argv[1])))
# server.stabilize()
value = 0
# server.start()
# server = Server()
first = [1] * 10
server = ClientNode(Address("127.0.0.1", 3000))
start_device_id = int(sys.argv[1]) * 10
while True:
	# server.start()
	# server.open_connection()
	next_time = time.time() + nextTime()
	while time.time() < next_time or sum(first) != 0 :
	# while True:
		for device in range(start_device_id, start_device_id + 10):
			server.insertKeyVal(str(device), str(value))
			if first[device - start_device_id]:
				first[device - start_device_id] = 0
				print("writing", sys.argv[1])
				f = open("devicefile.txt", "a")
				f.write("1")
				f.close()
				print("done writing", sys.argv[1])
			else:
				time.sleep(0.1)
			# time.sleep(1)
			test_device = str(device - random.randint(1, 5))
			# print("test lookup: ", device, test_device, server.lookUpKey(test_device))
		# exit(1)
		value += 1
	# server.join()

	# CLOSE CONNECTION
	# server.join()
	try:
		# server.join()
		server.close_connection()
		time.sleep(0.1)
	except AttributeError:
		# already closed
		pass
# loop.close()
