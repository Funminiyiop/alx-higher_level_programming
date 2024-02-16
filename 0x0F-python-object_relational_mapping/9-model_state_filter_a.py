#!/usr/bin/python3
"""
This script lists all State objects
that contain the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys
if __name__ == "__main__":
    """
    Access to the database and get a state
    from the database.
    """
    
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).filter(
        State.name.contains('a')).order_by(State.id).all()
    for place in state:
        print("{}: {}".format(place.id, place.name))
    session.close()
