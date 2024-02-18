#!/usr/bin/python3
'''
14-model_city_fetch_by_state.py: script that lists all City objects from the
database hbtn_0e_14_usa
Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password>
<database name>
'''

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for city, state in session.query(City, State).filter(City.state_id ==
                                                         State.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
