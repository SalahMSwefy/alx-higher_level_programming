#!/usr/bin/python3
'''
10-model_state_my_get.py: script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
Usage: ./10-model_state_my_get.py <mysql
username> <mysql password> <database name> <state name>
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
    state = session.query(State).filter(State.name == argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
