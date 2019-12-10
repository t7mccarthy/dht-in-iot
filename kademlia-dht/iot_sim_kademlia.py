import logging
import asyncio
import sys
import random
import time

from kademlia.network import Server


def generate_key_values(num_keys):
		# Generate a dictionary of N key-value pairs
		return_dict = {}
		for i in range(num_keys):
			key = "a" + str(i)
			value = str(i)
			return_dict[key] = value
		return return_dict


if __name__ == "__main__":
	if len(sys.argv) == 2:
		num_keys = int(sys.argv[1])
	else:
		print("Usage: python3 put_get_sim.py K (number of keys)")
		exit(1)

	# Loop initialization
	loop = asyncio.get_event_loop()
	loop.set_debug(True)
	# Server initialization
	server = Server()
	loop.run_until_complete(server.listen(8469))
	bootstrap_node = ("0.0.0.0", 8468)


	# _________________Inserting_________________
	sensors_dict = generate_key_values(num_keys)
	current_time = time.time()
	# Put calls
	loop.run_until_complete(server.bootstrap([bootstrap_node]))
	for key,value in sensors_dict.items():
		loop.run_until_complete(server.set(key, value))

	print(f"Inserted {len(sensors_dict)} key-value pairs into the DHT.")
	#put(sensors_dict, loop, "0.0.0.0", "8468")
	surpassed_time = time.time() - current_time
	print(f"Inserting {num_keys} key-value pairs took {surpassed_time} seconds.")



	# _______________Querying_______________

	keys_lst = list(sensors_dict.keys())
	random.shuffle(keys_lst)
	current_time = time.time()
	#get(keys_lst, loop, "0.0.0.0", "8468")
	for k in keys_lst:
		result = loop.run_until_complete(server.get(k))
	surpassed_time = time.time() - current_time
	print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} seconds.")


	server.stop()
	loop.close()
	print("Successfully exited.")
	exit(0)