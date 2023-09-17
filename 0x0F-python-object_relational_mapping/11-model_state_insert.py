#!/usr/bin/python3
""" add a record to the database """
from sqlalchemy import create_engine
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    con_str = "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3])
    engine = create_engine(con_str)
    Session = sessionmaker(bind=engine)
    session = Session()
    ill = State(name='Louisiana')
    session.add(ill)
    session.commit()
    print(ill.id)
