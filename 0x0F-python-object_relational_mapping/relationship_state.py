#!/usr/bin/python3
""" Object Relational database manipulation """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ creates table states using sqlalchemy
        and table columns: id and name
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True,
                unique=True, autoincrement='auto', nullable=False, )
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete-orphan',
                          back_populates='state')
