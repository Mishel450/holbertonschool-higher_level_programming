#!/usr/bin/python3
"""task-2"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    txt = "{}"
    db_conection = MySQLdb.connect(host='localhost', database=argv[3],
                                   user=argv[1], password=argv[2])
    cursor = db_conection.cursor()
    mySql_select_states = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(mySql_select_states)
    query = argv[4]
    for i in cursor.fetchall():
        if i[1] == query:
            print(txt.format(i))
    db_conection.close()
