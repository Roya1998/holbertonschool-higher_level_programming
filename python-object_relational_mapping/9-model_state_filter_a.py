#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter 'a' 
from the database hbtn_0e_6_usa, using SQLAlchemy.
The script takes 3 arguments: mysql username, mysql password,database name.
Results are sorted in ascending order by states.id.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# Import the model definitions
try:
    from model_state import Base, State
except ImportError:
    # Exit cleanly if the model definition is not found
    print("Error: Could not import State and Base from model_state.",
          file=sys.stderr)
    sys.exit(1)
if __name__ == "__main__":
    # Ensure correct number of arguments are passed
    if len(sys.argv) != 4:
        # Per instructions, no validation is strictly needed.
        pass
    # Extract command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    # Construct the database URL for connection
    db_url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, db_name
    )
    # Create the engine to connect to the MySQL database
    engine = create_engine(db_url, pool_pre_ping=True)
    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)
    # Create a Session
    session = Session()
    try:
        # Query all State objects:
        # 1. Filter: Use State.name.like('%a%') to match any state name
        #    containing the letter 'a'.
        # 2. Order: Sort the results by the 'id' attribute.
        states = session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id)\
                        .all()

        # Iterate over the results and print them in the required format
        for state in states:
            print("{}: {}".format(state.id, state.name))
    except Exception as e:
        # Catch any SQLAlchemy or database errors
        print(f"An error occurred during database operation: {e}",
              file=sys.stderr)
        sys.exit(1)
    finally:
        # Close the session
        session.close()
