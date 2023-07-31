#!/usr/bin/python3
"""model_states"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """Class State"""
    __tablename__ = 'some_table'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name =  Column(String(128), nullable=False)