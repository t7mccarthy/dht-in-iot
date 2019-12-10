import psycopg2
import subprocess
import time
import sys
import random

# connect_str = "dbname='iot_sensors' user='eric_bot' host='localhost' password='password'"
# # use our connection values to establish a connection
# conn = psycopg2.connect(connect_str)
# # create a psycopg2 cursor that can execute queries
# cursor = conn.cursor()
# # create a new table with a single column called "name"
# # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
# # run a SELECT statement - no data in there, but we can try it
# cursor.execute("SELECT * from sensors")
# conn.commit() # <--- makes sure the change is shown in the database
# rows = cursor.fetchall()
# print(rows)
# cursor.close()
# conn.close()
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
        print("Usage: python3 iot_sim_db.py K (number of keys)")
        exit(1)

    connect_str = "dbname='iot_sensors' user='eric_bot' host='localhost' password='password'"
    # use our connection values to establish a connection
    conn = psycopg2.connect(connect_str)
    # create a psycopg2 cursor that can execute queries
    cursor = conn.cursor()
    # create a new table with a single column called "name"
    # cursor.execute("""CREATE TABLE tutorials (name char(40));""")
    # run a SELECT statement - no data in there, but we can try it
    # cursor.execute("INSERT INTO sensors VALUES(key, value)")
    # conn.commit() # <--- makes sure the change is shown in the database
    # rows = cursor.fetchall()
    # print(rows)
    # cursor.close()
    # conn.close()

    # delete pre-existing table if there is one
    try:
        cursor.execute("DROP TABLE sensors;")
        conn.commit()
    except:
        pass

    # create table for sensor information
    cursor.execute("CREATE TABLE sensors (key varchar(100) NOT NULL, value varchar(100) NOT NULL);")
    conn.commit()

    # _________________Inserting_________________
    sensors_dict = generate_key_values(num_keys)
    current_time = time.time()
    # Put calls
    for key,value in sensors_dict.items():
        subprocess.run(["python3", "sensor_key_insertion.py", key, value])

    # block until done inserting
    num_rows = 0
    while (num_rows != len(sensors_dict)):
        cursor.execute("SELECT COUNT(*) FROM sensors;")
        conn.commit()
        num_rows = cursor.fetchall()[0][0]


    print(f"Inserted {len(sensors_dict)} key-value pairs into the database.")
    #put(sensors_dict, loop, "0.0.0.0", "8468")
    surpassed_time = time.time() - current_time
    print(f"Inserting {num_keys} key-value pairs took {surpassed_time} seconds.")

    cursor.close()
    conn.close()

    # _______________Querying_______________

    keys_lst = list(sensors_dict.keys())
    random.shuffle(keys_lst)
    current_time = time.time()

    for k in keys_lst:
        conn = psycopg2.connect(connect_str)
        cursor = conn.cursor()
        cursor.execute(f"SELECT value FROM sensors WHERE key = %s;", (k,))
        conn.commit()
        curr_value = cursor.fetchall()
        cursor.close()
        conn.close()

    surpassed_time = time.time() - current_time
    print(f"Checking {num_keys} key-value pairs (randomly) took {surpassed_time} seconds.")

    # cursor.execute("DROP TABLE sensors")
    # conn.commit()

    # cursor.close()
    # conn.close()
    print("Successfully exited.")
    exit(0)