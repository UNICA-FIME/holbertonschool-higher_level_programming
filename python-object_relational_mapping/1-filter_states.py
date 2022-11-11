#!/usr/bin/python3
'''
db_connection establece la conexion con la base de datos.
cursor crea un cursor para interactuar con la base de datos
cursor_leng muesta la contidad de item que tiene el objeto
list_1 convierte el objeto en un lista iterable

'''
import sys
import MySQLdb

db_connection = MySQLdb.connect(host="localhost", port=3306,
                                user=sys.argv[1], passwd=sys.argv[2],
                                db=sys.argv[3])
cursor = db_connection.cursor()
cursor_leng = cursor.execute("SELECT * FROM states ORDER BY states.id")
list_1 = list(cursor)
for item in range(0, cursor_leng):
    if list_1[item][1][0] == 'N':
        print(list_1[item])
