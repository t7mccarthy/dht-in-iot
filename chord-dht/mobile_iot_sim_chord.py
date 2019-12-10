import asyncio
import sys
import random
import time
import subprocess

from address import *
from iot_sim_chord import *
from chord import *



if __name__ == "__main__":

	num_keys = int(sys.argv[1])

	loop = asyncio.get_event_loop()
	# server = Node(Address("127.0.0.1", 3001), Address("127.0.0.1", 3000))


	# _________________Inserting_________________
	open('devicefile.txt', 'w').close()
	procs = []
	nodes = range(int(num_keys/10))
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
	def stop():
		for proc in procs:
			proc.kill()
		exit(0)
	i = 0
	# server = Node(Address("127.0.0.1", 3501), Address("127.0.0.1", 3500))
	server = ClientNode(Address("127.0.0.1", 3000))
	while i < 100:
		k = str(random.randint(0, num_keys))
		# print("Looking up")
		result = server.lookUpKey(k)
		if result == str(-1): continue
		# print("found key during eval", i, result)
		i += 1
		# if time.time() - current_time > 15: stop()
	surpassed_time = time.time() - current_time
	print(f"100 lookup operations with {num_keys} devices took {surpassed_time} seconds.")

	for proc in procs:
		proc.kill()

	loop.close()
	print("Successfully exited.")
	exit(0)