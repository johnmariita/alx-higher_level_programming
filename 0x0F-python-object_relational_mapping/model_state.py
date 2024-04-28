#!/usr/bin/python3
"""A script that defines the class state
used to create table states"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Definition of the class state"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    
    def __init__(self, name):
        self.name = name
