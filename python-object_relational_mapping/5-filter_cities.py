#!/usr/bin/python3
"""
 script that takes in the name of a state as an argument and lists
 all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM states \
             INNER JOIN cities ON states.id=cities.state_id \
             WHERE states.name=%s ORDER BY cities.id", (sys.argv[4],))
    query_row = cur.fetchall()
    item = 0
    for item in range(0, len(query_row)):
        if item < len(query_row)-1:
            print("{}".format(query_row[item][0]), end=", ")
    if (item != 0):
        print("{}".format(query_row[item][0]))
