import subprocess
import sys
import time


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py N (where N is the number of nodes)")
        sys.exit(1)
    N = int(sys.argv[1])
    if N < 1:
        print("N must be at least 1")
        sys.exit(1)
    
    print(f"This will open {N} gnome terminals.")
    command = ['gnome-terminal','--tab','-e',"python3 chord.py 3000"]
    for i in range(N-1):
        new_gnome = ['--tab','-e',f"python3 chord.py {3500 + i * 500} 3000"]
        command.extend(new_gnome)
    print('This is the comamnd:', command)

    # for i in range(N-1):
    #     subprocess.run(f"python3 chord.py {3500 + i * 500} 3000", shell=True)
    current_time = time.time()
    subprocess.run(command)
    surpassed_time = time.time() - current_time
    print(f"Initializing {N} nodes took {surpassed_time} milliseconds.")
