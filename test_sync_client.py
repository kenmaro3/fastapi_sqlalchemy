from sqlalchemy.ext.asyncio import create_async_engine, Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import Result
from sqlalchemy import select
from sqlalchemy.orm import joinedload

import api.models.user as user_model

#ASYNC_DB_URL = "mysql+aiomysql://root@localhost:3306/test?charset=utf8"
SYNC_DB_URL = "mysql+pymysql://root@localhost:3306/test?charset=utf8"
#ASYNC_DB_URL = 'sqlite:///sample_db.sqlite3' # cannot be async

# async_engine = create_async_engine(ASYNC_DB_URL, echo=True)
# async_session = sessionmaker(
#     autocommit=False, autoflush=False, bind=async_engine, class_=Session
# )
engine = create_engine(SYNC_DB_URL, echo=True)

Session = sessionmaker(
    engine
)


with Session() as session:
    users = session.query(user_model.User).options(joinedload(user_model.User.projects))
    print(users.all())
    res = users.all()
    for el in res:
        print(el.name)
    

# def test(): result: Result = await db.execute(
#         select(user_model.User).filter()
#         .options(joinedload(user_model.User.projects))
#     )
#     return result
