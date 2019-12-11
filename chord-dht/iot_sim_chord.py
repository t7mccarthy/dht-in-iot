#!/bin/python3
import sys
import json
import socket
import random
import time

import threading
from config import *
from network import *
from chord import *
from address import *

def requires_connection(func):
	def inner(self, *args, **kwargs):
		self.open_connection()
		ret = func(self, *args, **kwargs)
		self.close_connection()
		return ret
	return inner


class ClientNode(object):
	def __init__(self,RemoteAddress = None):
		self._serverAddress = RemoteAddress
		self.client_running = True
	
	def open_connection(self):
		self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self._socket.connect((self._serverAddress.ip, self._serverAddress.port))

	def close_connection(self):
		self._socket.close()
		self._socket = None

	def send(self, msg):
		send_to_socket(self._socket,msg)
		self.last_msg_send_ = msg

	def recv(self):
		return read_from_socket(self._socket)
	
	@requires_connection
	def lookUpKey(self,key):
		self.send('lookUpKey '+key)
		return self.recv()

	@requires_connection
	def insertKeyVal(self,key,value):
		self.send('insertKeyVal '+key+' '+value)	
		return self.recv()

	def automated_lookup(self, key, return_result = True):
		returnvalue = self.lookUpKey(key)
		if return_result:
			log("Returning lookup" + str(returnvalue), key)
			return returnvalue
		if returnvalue == '-1':
			print("Key :",key," not found !!")
	
	def automated_insert(self, key, value):
		# Insert a key value pair into the DHT
		returnvalue = self.insertKeyVal(key,value)
		print("Key : ",key," :: Value : ",value," inserted")
	
	def automated_load(self, sensors_dict):
		# Insert many key value pairs into the DHT
		for key,value in sensors_dict.items():
			self.insertKeyVal(key,value)
		print(f"Inserted {len(sensors_dict)} key-value pairs into the DHT.")

	def generate_key_values(self, num_keys):
		# Generate a dictionary of N key-value pairs
		return_dict = {}
		for i in range(num_keys):
			key = "a" + str(i)
			value = str(i)
			return_dict[key] = value
		return return_dict

	def automated_script(self, num_keys):
		sensors_dict = self.generate_key_values(num_keys)
		current_time = time.time()
		# Insert key-value pairs from dictionary
		self.automated_load(sensors_dict)
		surpassed_time = time.time() - current_time
		print(f"Inserting {num_keys} key-value pairs took {surpassed_time} seconds.")
		# Check on random keys with flexible queries
		keys_lst = list(sensors_dict.keys())
		random.shuffle(keys_lst)
		current_time = time.time()
		for k in keys_lst:
			self.automated_lookup(k, False)
		surpassed_time = time.time() - current_time
		print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} seconds.")
		print("Successfully exited.")
		exit(0)

if __name__ == "__main__":
	import sys
	local = ClientNode(Address(sys.argv[1], sys.argv[2]))
	local.automated_script(int(sys.argv[3]))		# arv[3] is num of keys