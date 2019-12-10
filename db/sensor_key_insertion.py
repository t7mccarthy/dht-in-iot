import psycopg2
import sys


if __name__ == "__main__":

	key = sys.argv[1]
	value = sys.argv[2]

	connect_str = "dbname='iot_sensors' user='eric_bot' host='localhost' password='password'"
	# use our connection values to establish a connection
	conn = psycopg2.connect(connect_str)
	# create a psycopg2 cursor that can execute queries
	cursor = conn.cursor()
	# create a new table with a single column called "name"
	# cursor.execute("""CREATE TABLE tutorials (name char(40));""")
	# run a SELECT statement - no data in there, but we can try it
	cursor.execute(f"INSERT INTO sensors VALUES(%s, %s);", (key, value))
	conn.commit() # <--- makes sure the change is shown in the database
	# rows = cursor.fetchall()
	# print(rows)
	# cursor.execute("SELECT COUNT(*) FROM sensors")
	# rows = cursor.fetchall()
	# print(rows[0][0])
	cursor.close()
	conn.close()


	exit(0)