#!/usr/bin/python3
"""
ns the class definition of a State and an instance Base = declarative_base()
"""
from SQLAlchemy import Column, Integer, String, MetaData
import SQLAlchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)

class State(Base):
    """

    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
