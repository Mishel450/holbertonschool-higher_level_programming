#!/usr/bin/python3
"""7-task"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from model_state import State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    st = session.query(City, State).filter(City.state_id == State.id).order_by(City.id)
    for state, city in st:
        print("{}: ({}) {}".format(city.name, city.id, state.name))