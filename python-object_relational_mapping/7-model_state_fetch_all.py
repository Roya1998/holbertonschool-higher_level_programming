#!/usr/bin/python3
"""
model_state.py: Defines the State class and an instance of Base for SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
# Define the base class for declarative class definitions
Base = declarative_base()
class State(Base):
    """
    Represents a state for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to map to.
        id (sqlalchemy.Integer): The state's ID (primary key).
        name (sqlalchemy.String): The state's name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)