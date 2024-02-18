#!/usr/bin/python3
'''
model_state.py: Python file similar to model_state.sql that defines a
State class and an instance Base = declarative_base():
'''
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class State(Base):
    '''
    State class with id and
    name attributes
    '''
    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, nullable=False)
    name = Column('name', VARCHAR(128), nullable=False)
