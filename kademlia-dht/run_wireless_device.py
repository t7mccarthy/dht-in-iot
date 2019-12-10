import logging
import asyncio
import sys

from kademlia.network import Server

import math
import random
import time

def nextTime(rateParameter = 1/5):
    return -math.log(1.0 - random.random()) / rateParameter

loop = asyncio.get_event_loop()
loop.set_debug(True)

value = 0
# server = Server()
bootstrap_node = ("0.0.0.0", 8469 + int(sys.argv[1]))
first = [True] * 10
start_device_id = int(sys.argv[1]) * 10
while True:
	server = Server()
	loop.run_until_complete(server.listen(8470 + int(sys.argv[1])))
	loop.run_until_complete(server.bootstrap([bootstrap_node]))
	next_time = time.time() + nextTime()
	# while time.time() < next_time:
	while True:
		for device in range(start_device_id, start_device_id + 10):
			result = loop.run_until_complete(server.set(str(device), value))
			if result and first[device - start_device_id]:
				first[device - start_device_id] = False	
				print("writing", sys.argv[1])
				f = open("devicefile.txt", "a")
				f.write("1")
				f.close()
				print("done writing", sys.argv[1])
			else:
				time.sleep(0.25)
		value += 1
	server.stop()
loop.close()
