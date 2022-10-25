from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy
import json

import test

# declaration
Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///sample_db.sqlite3', echo=True)



app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/projects/{user_id}")
async def projects(user_id: int):
    session = test.mock_get_session(engine)
    projects = test.get_projects(session, user_id)
    print("\n\n=========here")
    print(projects)
    projects_name = []
    for el in projects:
        projects_name.append(el.name)

    return {"projects_name": json.dumps(projects_name)}
