#!/usr/bin/python3
"""Lists all State and corresponding City objects"""

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Create MySQL connection string
    mysql_conn = (
            f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}"
            f"@localhost:3306/{sys.argv[3]}"
            )

    # Create SQLAlchemy engine
    engine = create_engine(mysql_conn, pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State and corresponding City objects
    states = session.query(State).order_by(State.id).all()

    # Print State and City details
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda x: (x.id)):
            print("    {}: {}".format(city.id, city.name))

    # Close session
    session.close()
