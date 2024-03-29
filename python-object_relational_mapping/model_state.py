#!/usr/bin/python3
"""
contains the class definition of a State and
an instance Base = declarative_base()

"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    define columns as class attributes.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=True)
    name = Column(String(128), nullable=True)
