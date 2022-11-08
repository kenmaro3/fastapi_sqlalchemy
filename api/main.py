from fastapi import FastAPI

from api.routers import user
from api.routers import project
from api.routers import model
from api.routers import scaler
from api.routers import optimization
from api.routers import data

app = FastAPI()
app.include_router(user.router)
app.include_router(project.router)
app.include_router(model.router)
app.include_router(scaler.router)
app.include_router(optimization.router)
app.include_router(data.router)