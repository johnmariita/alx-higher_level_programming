#!/usr/bin/python3
"""Script that lists all the cities with the states
they are from"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City

if __name__ == "__main__":
    usr = sys.argv[1]
    pwd = sys.argv[2]
    db = sys.argv[3]
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}"
    engine = create_engine(url.format(usr, pwd, db))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print(f"{city.id}: {city.name}->{city.state.name}")
