#!/usr/bin/python3
""" handles city manipulation of city objects
    with the sql alchemy orm
"""
from sqlalchemy import create_engine
from model_city import Base, City
from model_city import State
from sqlalchemy.orm import relationship, sessionmaker
from sys import argv


if __name__ == "__main__":
    con_str = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(con_str)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(City, State).filter(City.state_id == State.id).all()
    for c, s in rows:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
