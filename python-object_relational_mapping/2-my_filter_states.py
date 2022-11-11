#!/usr/bin/python3
"""
write script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb
if __name__ == '__main__':
    db_connection = MySQLdb.connect(host="localhost", port=3306,
                                    user=sys.argv[1], passwd=sys.argv[2],
                                    db=sys.argv[3])
    cur = db_connection.cursor()
    len_obj = cur.execute("SELECT * FROM  states ORDER BY states.id ASC")
    list_obj = list(cur)
    for item in range(0, len_obj):
        if list_obj[item][1] == sys.argv[4]:
            print("({}, '{}')".format(list_obj[item][0], list_obj[item][1]))
