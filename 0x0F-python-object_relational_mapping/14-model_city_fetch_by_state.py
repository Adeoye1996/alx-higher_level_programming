#!/usr/bin/python3
"""
List all State objects with a corresponding City
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # MySQL connection string
    mysql = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

    # Create SQLAlchemy engine
    engine = create_engine(mysql)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State objects with corresponding City
    states_cities = session.query(State, City).filter(State.id == City.state_id).order_by(City.id).all()

    # Print State and City details
    for state, city in states_cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close session
    session.close()
