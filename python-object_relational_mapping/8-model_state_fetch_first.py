#!/usr/bin/python3
"""7-task"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from model_state import State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    connect = engine.connect()
    states = sqlalchemy.select(State.id, State.name)
    res = connect.execute(states).fetchone()

    if res is None:
        print("Nothing")
    else:
        print("{}: {}".format(res[0], res[1]))
