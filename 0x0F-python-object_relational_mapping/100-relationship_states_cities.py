#!/usr/bin/python3
""" add a record to the database """
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_city import City
from relationship_state import State, Base
# Base = declarative_base


if __name__ == "__main__":
    con_str = "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3])
    engine = create_engine(con_str)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    stat = State(name='California')
    stat.cities = [City(name='San Francisco')]
    session.add(stat)
    session.commit()
