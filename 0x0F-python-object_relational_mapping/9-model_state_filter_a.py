#!/usr/bin/python3
'''
9-model_state_filter_a.py: script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
Usage: ./9-model_state_filter_a.py <mysql username> <mysql password>
<database name>
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(state.id, state.name))
    session.close()
