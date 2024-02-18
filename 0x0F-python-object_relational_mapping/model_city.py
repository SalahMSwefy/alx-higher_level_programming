#!/usr/bin/python3
'''
model_city.py: Python file similar to model_state.py that defines a
City class and an instance Base = declarative_base():
'''

from sqlalchemy import create_engine, VARCHAR, Column, Integer
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base, State

Base = declarative_base()


class City(Base):
    '''
    City class with id, name, and state_id attributes
    '''
    __tablename__ = 'cities'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', VARCHAR(128), nullable=False)
    state_id = Column('state_id', Integer, ForeignKey('states.id'),
                      nullable=False)

    def __init__(self, name, state_id):
        self.name = name
        self.state_id = state_id

    def __repr__(self):
        return "<City(name='%s')>" % self.name

    def __str__(self):
        return "{}".format(self.name)

    def __del__(self):
        pass


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
