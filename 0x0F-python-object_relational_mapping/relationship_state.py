#!/usr/bin/python3
"""
Module Docs
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, Integer, MetaData


Base = declarative_base(metadata=MetaData)


class State(Base):
    """
    Class Docs
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,unique=True)
    name = Column(String(128), nullable=False)
