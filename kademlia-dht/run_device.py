import logging
import asyncio
import sys

from kademlia.network import Server

import time

loop = asyncio.get_event_loop()
loop.set_debug(True)

value = 0
server = Server()
bootstrap_node = ("0.0.0.0", 8469 + int(sys.argv[1]))

loop.run_until_complete(server.listen(8470 + int(sys.argv[1])))
loop.run_until_complete(server.bootstrap([bootstrap_node]))

f = open("devicefile.txt", "a")

for device in range(int(sys.argv[1]) * 10, int(sys.argv[1]) * 10 + 10):
	try:
		print ("inserting", device)
		result = loop.run_until_complete(server.set(device, value))
		f.write("1")
	except:
		pass
f.close()
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    loop.close()
