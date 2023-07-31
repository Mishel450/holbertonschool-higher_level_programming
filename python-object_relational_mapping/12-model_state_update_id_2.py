#!/usr/bin/python3
"""12-task"""
from sys import argv
import sqlalchemy
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_modify = session.query(State).filter_by(id=2).first()
    state_to_modify.name = 'New Mexico'
    session.commit()
    session.close()
