import logging
import asyncio
import sys

from kademlia.network import Server

print("SETTING UP NEW NODE:")

loop = asyncio.get_event_loop()
loop.set_debug(True)

server = Server()
loop.run_until_complete(server.listen(int(sys.argv[3])))
bootstrap_node = (sys.argv[1], int(sys.argv[2]))
loop.run_until_complete(server.bootstrap([bootstrap_node]))
# loop.run_until_complete(server.set(sys.argv[3], sys.argv[4]))
# server.stop()
# loop.close()
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    server.stop()
    loop.close()