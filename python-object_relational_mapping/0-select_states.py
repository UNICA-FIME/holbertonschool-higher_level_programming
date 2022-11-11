#!/usr/bin/python3
"""
module sys use for arguments argv
MySQLdb conection the mysql server
cur is objet cursor
cur.execute rum query

"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_connection = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for item in cur:
        print(item)
