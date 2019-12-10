import subprocess
import time
import sys

N = int(sys.argv[1])
print(f"This will initialize {N} gnome terminals.")
command = ['gnome-terminal','--tab','-e',"python3 start_network.py"]
for i in range(N):
	new_port = 8469 + i
	new_gnome = ['--tab','-e',f"python3 new_node.py 0.0.0.0 8468 {new_port}"]
	command.extend(new_gnome)
print('This is the comamnd:', command)
current_time = time.time()
subprocess.run(command)
surpassed_time = time.time() - current_time
print(f"Initializing {N} nodes took {surpassed_time} seconds.")