# Simiulating Distributed Hash Tables for Ad-hoc Wireless IoT Communication: https://github.com/t7mccarthy/dht-iot

### Harvard CS 143 Final Project
### Developed by Tom McCarthy and Eric Lin
#### December 9th, 2019


In this Git Repo, we present implementations of proof-of-concept for the following concepts and their appliation in mobile networks:
- Chord DHT
- Kadmelia DHT
- Traditional centralized database approach.

Running the DHT simulations is only supported in linux OS. Using a VM is highly reccomended; some of the process management here is definitely not entirely safe.

## Chord DHT
A basic implementation of a chord DHT used in IOT communication simulations.

### Usage
Run `setup_network.py N` before running anything else to initialize the network with N nodes. This will open N gnome terminals, which must be closed before running the program again. Testing was carried out with 3 initial network nodes, but any number would work.

Run `iot_sim_chord.py 127.0.0.1 3000 N` to test how long it takes to insert and check N value-key pairs.

Run `mobile_iot_sim_chord N` to simulate a mobile/wireless network with nodes going offline according to a poisson traffic model. After terminating, the program will report how long it took to lookup 100 random keys.

### Important Files
- `setup_network.py` initialize network, run each node as a seperate process in a seperate gnome terminal.
- `chord.py` create and run a network node.
- `iot_sim_chord.py` create client node bootstrapped to given ip/port, record timing of inserts and lookups.
- `mobile_iot_sim_chord.py` create subprocess for each set of devices (runs `run_wireless_device.py`), create network node for each subprocess, record how long it takes to query 100 keys.
- `run_wireless_device.py` initializesnew node, add key-value pair for each device onto the dht, continually update key-value pairs while going offline according to a poisson traffic model (simulates wirelessly connected IOT devices).


## Kademila DHT
Python Kademlia API (a basic implementation of a Kademlia DHT: https://kademlia.readthedocs.io/en/latest/) used in IOT communication simulations.

### Usage
Run `setup_network.py N` before running anything else to initialize the network with N nodes. This will open N gnome terminals, which must be closed before running the program again. Testing was carried out with 3 initial network nodes, but any number would work.

Run `iot_sim_kademlia.py N` to test how long it takes to insert and check N value-key pairs.

Run `iot_sim_kad N` to set N key-value pairs on the DHT and report how long it took to lookup 100 random keys.

Run `mobile_iot_sim_kad N` to simulate a mobile/wireless network with nodes going offline according to a poisson traffic model. After terminating, the program will report how long it took to lookup 100 random keys. For large Ns, this will take a while and throw some errors, but it adjusts and finished eventially.

### Important Files
- `setup_network.py` initialize network, run each node as a seperate process in a seperate gnome terminal.
- `start_network.py` create and run first network node.
- `new_node.py` create and run a network node.
- `iot_sim_kademlia.py` create node, record timing of inserts and lookups.
- `mobile_iot_sim_kad.py` creates subprocess for each set of devices (runs `run_wireless_device.py`), create network node for each subprocess, record how long it takes to query 100 keys.
- `run_wireless_device.py` initializes new node, adds key-value pair for each device onto the dht, continually updates key-value pairs while going offline according to a poisson traffic model (simulates wirelessly connected IOT devices).
- `iot_sim_kad` creates subprocess for each set of devices (runs `run_device.py`), create network node for each subprocess, record how long it takes to query 100 keys.
- `run_device.py` initializes new node, adds key-value pair for each device onto the dht.


## Centralized Database
IOT communication simulations using a traditional centralized PostgreSQL database. This assumes you have set up a local Postgres database called `iot_sensors` and are running it on localhost. Our implementation also requires a database user `eric_bot` who has all privileges on `iot_sensors` and has password `password`.

### Usage
Run `iot_sim_db.py N` to test how long it takes to insert and lookup 100 random keys in a network of N devices.

Run `insert_lookup_db.py N` to test how long it takes to insert and lookup N key-value pairs.

### Important Files
- `iot_sim_db.py` create subprocess for each device (runs `run_sensor.py`), create a row in the database for each device (updated continually), record how long it takes to query 100 keys.
- `run_sensor.py` connect to database, add row for each device onto the database, continually update row (simulating continually updating sensor data).
- `insert_lookup_db.py` create subprocess for each device (runs `run_sensor.py`), create a row in the database for each device, record how long it takes to query all devices in random order.
- `run_sensor.py` connect to database, add row onto the database for key-value pair.


Old commits in https://github.com/t7mccarthy/dht-iot-old.
