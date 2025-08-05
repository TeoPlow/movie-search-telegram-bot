from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import os

Base = declarative_base()

class UserRequestHistory(Base):
    __tablename__ = "users_request_history"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    date = Column(DateTime, nullable=False)
    movie_info = Column(String, nullable=False)


def create_database():
    if not os.path.exists("database/database.db"):
        engine = create_engine("sqlite:///database/database.db")
        Base.metadata.create_all(engine)
        print("LOG: База данных и таблица созданы")
    else:
        print("LOG: База данных уже существует")

