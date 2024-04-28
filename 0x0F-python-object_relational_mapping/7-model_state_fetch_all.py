#!/usr/bin/python3
"""A Script that lists all the states from the table states"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                       sys.argv[2], sys.argv[3]), pool_pre_ping=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).all()
for state in states:
    print(f"{state.id}: {state.name}")
