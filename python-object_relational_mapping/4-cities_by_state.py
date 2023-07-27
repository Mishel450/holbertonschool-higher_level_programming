#!/usr/bin/python3
"""task-4 """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conection = MySQLdb.connect(host='localhost', database=argv[3],
                                   user=argv[1], password=argv[2])
    cursor = db_conection.cursor()

    cursor.execute("SELECT * FROM cities ORDER BY id ASC")

    for i in cursor.fetchall():
        print(i)
    db_conection.close()
