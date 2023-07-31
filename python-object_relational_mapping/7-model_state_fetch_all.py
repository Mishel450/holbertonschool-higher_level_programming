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
    states = sqlalchemy.select(State.id, State.name).order_by(State.id)
    res = connect.execute(states).fetchall()

    for states in res:
        print("{}: {}".format(states[0], states[1]))
