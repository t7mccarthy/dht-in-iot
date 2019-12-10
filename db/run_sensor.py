import psycopg2
import sys
import time


if __name__ == "__main__":

	key = sys.argv[1]
	value = sys.argv[2]

	# connect_str = "dbname='iot_sensors' user='eric_bot' host='localhost' password='password'"
	# use our connection values to establish a connection
	# conn = psycopg2.connect(connect_str)
	# create a psycopg2 cursor that can execute queries
	# cursor = conn.cursor()
	first = True

	while True:
		connect_str = "dbname='iot_sensors' user='eric_bot' host='localhost' password='password'"
		# use our connection values to establish a connection
		conn = None
		while True:
			try:
				conn = psycopg2.connect(connect_str)
				break
			except:
				pass
		# create a psycopg2 cursor that can execute queries
		cursor = conn.cursor()
		# create a new table with a single column called "name"
		# cursor.execute("""CREATE TABLE tutorials (name char(40));""")
		# run a SELECT statement - no data in there, but we can try it
		cursor.execute(f"SELECT value FROM sensors WHERE key = %s;", (key,))
		conn.commit()
		curr_value = cursor.fetchall()
		# print(curr_value)
		if curr_value != []:
			cursor.execute(f"DELETE FROM sensors WHERE key = %s;", (key,))
			conn.commit()
			# time.sleep(0.1)
		# try: pass
			# cursor.execute(f"DELETE FROM sensors WHERE sensors.key = {key}")
			# conn.commit()
		# except:
		# 	pass

		cursor.execute(f"INSERT INTO sensors VALUES(%s, %s);", (key, value))
		conn.commit() # <--- makes sure the change is shown in the database

		if first:
			f = open("devicefile.txt", "a")
			f.write("1")
			f.close()
			first = False
		# rows = cursor.fetchall()
		# print(rows)
		# cursor.execute("SELECT COUNT(*) FROM sensors")
		# rows = cursor.fetchall()
		# print(rows[0][0])
		cursor.close()
		conn.close()
		# time.sleep(0.25)
	# cursor.close()
	# conn.close()


	