#!/usr/bin/python3
"""
This script prints the State object id
with the name passed as argument
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
        State.name == sys.argv[4]).first()
    try:
        print("{}".format(state.id))
    except:
        print("Not found")
    session.close()
