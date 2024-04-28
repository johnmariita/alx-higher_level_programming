#!/usr/bin/python3
"""A Script that searches for a state in the database"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    safe_state = sys.argv[4].split("'")[0]
    state = session.query(State).filter(State.name == safe_state).one_or_none()
    if state:
        print(f"{state.id}: {state.name}")
    else:
        print("Not found")
