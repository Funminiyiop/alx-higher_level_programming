#!/usr/bin/python3
# Lists all City objects from the database hbtn_0e_101_usa.
# Usage: ./102-relationship_cities_states_list.py <mysql username> /
#                                                 <mysql password> /
#                                                 <database name>

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys
if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    citys = session.query(City).order_by(City.id).all()
    for city in citys:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
