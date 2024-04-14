#!/usr/bin/python3
"""
Updates the name of a State object with id=2 to 'New Mexico'
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, database = sys.argv[1:]

    # Create MySQL connection string
    mysql = f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"

    # Create SQLAlchemy engine
    engine = create_engine(mysql)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Update name of State with id=2 to 'New Mexico'
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()
        print("State name updated successfully.")
    else:
        print("State with id=2 not found.")

    # Close session
    session.close()
