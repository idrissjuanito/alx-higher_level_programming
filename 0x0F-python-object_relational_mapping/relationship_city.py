#!/usr/bin/python3
""" City object class for sqlalchemy orm """
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from relationship_state import State, Base
# Base = declarative_base()


class City(Base):
    """ table cities and schema definition """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, autoincrement=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
