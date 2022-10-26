import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from db import Base

ASYNC_DB_URL = "mysql+pymysql://root@localhost:3306/test?charset=utf8"
engine = sqlalchemy.create_engine(ASYNC_DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()