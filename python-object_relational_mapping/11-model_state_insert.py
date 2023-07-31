#!/usr/bin/python3
"""11-task"""
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
    st = State(name='Louisiana')
    session.add(st)
    session.commit()
    print(st.id)
