# reads from socket until "\r\n"
def read_from_socket(s):
	result = ""
	while 1:
		data = s.recv(1024)
		data = data.decode('utf-8')
		if data[-2:] == "\r\n":
			result += data[:-2]
			break
		result += data

	return result

# sends all on socket, adding "\r\n"
def send_to_socket(s, msg):
	st = str(msg) + "\r\n"
	s.sendall(st.encode('utf-8'))
