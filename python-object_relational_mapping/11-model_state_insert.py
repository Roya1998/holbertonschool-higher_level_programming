#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)
    username, password, db_name, state_name = sys.argv[1], sys.argv[2], \
                                                sys.argv[3], sys.argv[4]
    # Create engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:'
                           f'3306/{db_name}', pool_pre_ping=True)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for the state by name
    state = session.query(State).filter(State.name == state_name).first()

    # If state is found, print its id, else print "Not found"
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
