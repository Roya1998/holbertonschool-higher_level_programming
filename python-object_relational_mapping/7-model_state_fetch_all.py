#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    # Create engine to connect to the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1],  # MySQL username
            sys.argv[2],  # MySQL password
            sys.argv[3]   # Database name
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states ordered by id
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print(f"{state.id}: {state.name}")
