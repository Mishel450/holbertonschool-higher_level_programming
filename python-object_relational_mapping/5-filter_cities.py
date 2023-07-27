#!/usr/bin/python3
"""task-4 """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db_conection = MySQLdb.connect(host='localhost', database=argv[3],
                                   user=argv[1], password=argv[2])
    cursor = db_conection.cursor()
    mySql_select_states = """SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id ORDER BY id ASC"""
    cursor.execute(mySql_select_states)
    query = argv[4]
    my_list = []
    for i in cursor.fetchall():
        if i[2] == query:
            my_list.append(i[1])
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            print (my_list[i], end="")
        else:
            print(my_list[i], end=", ")
    print()
    db_conection.close()
