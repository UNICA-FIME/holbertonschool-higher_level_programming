#!/usr/bin/python3
"""cript that takes in arguments and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument. But this time, write one
   that is safe from MySQL injections!
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM states WHERE states.name=%s", (sys.argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db_connection.close()
