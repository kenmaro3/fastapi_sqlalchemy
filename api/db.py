#from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#ASYNC_DB_URL = "mysql+aiomysql://root@localhost:3306/test?charset=utf8"
SYNC_DB_URL = "mysql+pymysql://root@localhost:3306/test?charset=utf8"
#ASYNC_DB_URL = 'sqlite:///sample_db.sqlite3' # cannot be async

#async_engine = create_async_engine(SYNC_DB_URL, echo=True)
engine = create_engine(SYNC_DB_URL, echo=True)
async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = declarative_base()


def get_db():
    with async_session() as session:
        yield session