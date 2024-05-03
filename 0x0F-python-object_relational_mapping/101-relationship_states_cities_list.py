#!/usr/bin/python3
"""Script that prints the States with their related cities"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(url.format(usr, pwd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).all()
    for state in states:
        print(f"{state.id}: {state.name}")
        for i in range(len(state.cities)):
            print(f"    {state.cities[i].id}: {state.cities[i].name}")
