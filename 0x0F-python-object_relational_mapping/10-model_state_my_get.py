#!/usr/bin/python3
"""
Searches for a State object by name in the database.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state_name = sys.argv[1:]

    # Create MySQL connection string
    mysql = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    # Create SQLAlchemy engine
    engine = create_engine(mysql)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for State object by name
    state = session.query(State).filter(State.name == state_name).first()

    # Display result
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
