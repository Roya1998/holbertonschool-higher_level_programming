#!/usr/bin/python3
"""
Changes the name of a State object in the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(username, password, database),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        # Find the state with id = 2
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = "New Mexico"
            session.commit()
    finally:
        session.close()
