#!/usr/bin/python3
"""
Lists all state objects from the database
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Get the database parameters from the command line arguments
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Create a database connection
    engine = create_engine(
        f'mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    # Bind the engine to the metadata of the class
    Base.metadata.create_all(engine)

    session = Session()
    # Quary all state object and sort by state.id
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()

    # Print each state thst contains letter a
    for each_state in states_with_a:
        print(f"{each_state.id}: {each_state.name}")

    # Close all session
    session.close()
