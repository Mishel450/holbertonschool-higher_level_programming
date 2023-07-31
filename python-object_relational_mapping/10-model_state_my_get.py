#!/usr/bin/python3
"""7-task"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from model_state import State

flag = 0

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    connect = engine.connect()
    states = sqlalchemy.select(State.id, State.name).order_by(State.id)
    res = connect.execute(states).fetchall()

    for st in res:
        if st[1] == argv[4]:
            print("{}".format(st[0]))
            flag = 1
    if flag == 0:
        print("Not found")
