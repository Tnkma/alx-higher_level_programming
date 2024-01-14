#!/usr/bin/python3
"""
Add a new state objects from the database
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
    new_state = 'Louisiana'

    # Create a database connection
    engine = create_engine(
        f'mysql+mysqldb://{user_name}:{password}@localhost:3306/{db_name}')

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    # Bind the engine to the metadata of the class
    Base.metadata.create_all(engine)

    session = Session()
    # Create a new state object
    create_object = State(name=new_state)
    # Add to the database
    session.add(create_object)
    # Commit to the database
    session.commit()

    # Print the state.id
    print(f"{create_object.id}")

    # Close all session
    session.close()
