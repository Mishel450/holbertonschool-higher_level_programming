#!/usr/bin/python3
"""task-0"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conection = MySQLdb.connect(host='localhost', database=argv[3],
                                   user=argv[1], password=argv[2])
    cursor = db_conection.cursor()
    mySql_select_states = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(mySql_select_states)
    for i in cursor.fetchall():
        print(i)
    db_conection.close()
