__author__ = 'Arjen'
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from settings import db_con, db_echo


Base = declarative_base()
engine = create_engine(db_con, echo=db_echo)
Session = scoped_session(sessionmaker(bind=engine))

