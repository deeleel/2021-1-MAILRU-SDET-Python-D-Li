from enum import auto
from sqlalchemy import Column, Integer, String, SmallInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.elements import Null

Base = declarative_base()

class Users(Base):
    __tablename__ = 'test_users'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    username = Column(String(16), default=Null, unique=True)
    password = Column(String(255), nullable=False)
    email = Column(String(64), nullable=False, unique=True)
    access = Column(SmallInteger, default=Null)
    active = Column(SmallInteger, default=Null)
    start_active_time = Column(DateTime, default=Null)


    

