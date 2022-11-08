import asyncio
from sqlalchemy.orm import Session


import api.cruds.user as user_cruds
import api.cruds.project as project_cruds
import api.cruds.model as model_cruds
import api.cruds.scaler as scaler_cruds

from api.db import get_db

from api.schemas.user import UserCreateRequest

async def test():
    with Session(get_db) as session:
        user = await user_cruds.create_user(session, tmp)
    print(user)


if __name__ == "__main__":
    print("hello, world")
    tmp = UserCreateRequest(name="kenmaro", password="1234")
    asyncio.run(test())
    
