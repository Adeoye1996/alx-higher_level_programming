#!/usr/bin/python3
"""
Deletes all State objects with a name containing 'a'
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

    # Delete State objects with name containing 'a'
    num_deleted = session.query(State).filter(State.name.contains('a')).delete(synchronize_session=False)
    session.commit()

    print(f"{num_deleted} State(s) deleted.")

    # Close session
    session.close()

