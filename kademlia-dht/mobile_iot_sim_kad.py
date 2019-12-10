import logging
import asyncio
import sys
import random
import time
import subprocess

from kademlia.network import Server


if __name__ == "__main__":
	if len(sys.argv) == 2:
		num_keys = int(sys.argv[1])
	else:
		print("Usage: python3 put_get_sim.py K (number of devices)")
		exit(1)

	loop = asyncio.get_event_loop()
	# loop.set_debug(True)
	# Server initialization
	server = Server()
	loop.run_until_complete(server.listen(8469))
	bootstrap_node = ("0.0.0.0", 8468)


	# _________________Inserting_________________
	open('devicefile.txt', 'w').close()
	procs = []
	nodes = range(int(num_keys/10) + 1)
	for key in nodes:
		proc = subprocess.Popen(["python3", "run_wireless_device.py", str(key)], stdin=None, stdout=None, stderr=None, close_fds=True)
		procs.append(proc)
		# subprocess.run(["python3", "run_device.py", str(key)])

	# time.sleep(100)
	l = 0
	while l < num_keys:
		with open('devicefile.txt') as infile:
		# print(l)
			l = sum([len(line) for line in infile])
		pass
	print("done", l)
	print(f"Inserted {num_keys} key-value pairs into the DHT.")

	# _________________Querying_________________
	current_time = time.time()

	i = 0
	while i < 100:
		k = str(random.randint(0, num_keys))
		result = loop.run_until_complete(server.get(k))
		if not result: continue
		print(i, result)
		i += 1
	surpassed_time = time.time() - current_time
	print(f"100 lookup operations with {num_keys} devices took {surpassed_time} seconds.")

	for proc in procs:
		proc.kill()

	server.stop()
	loop.close()
	print("Successfully exited.")
	exit(0)