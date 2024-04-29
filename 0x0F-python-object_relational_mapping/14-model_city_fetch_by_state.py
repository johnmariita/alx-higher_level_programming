#!/usr/bin/python3
"""A script that joins two tables"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from model_city import Base, City
from model_state import State
import sys


if __name__ == "__main__":
    conn = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(conn.format(sys.argv[1],
                           sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    State.cities = relationship("City", order_by=City.id,
                                back_populates="state")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State, City).filter(State.id == City.state_id).all()
    for row in rows:
        print(f"{row[0].name}: ({row[1].id}) {row[1].name}")
