import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from api.db import Base
from api.models.user import User
from api.models.user_project import UserProject
from api.models.project import Project

ASYNC_DB_URL = "mysql+pymysql://root@localhost:3306/test?charset=utf8"
engine = sqlalchemy.create_engine(ASYNC_DB_URL, echo=True)

def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()