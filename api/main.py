from fastapi import FastAPI

from api.routers import user
#from api.routers import intermediate_user_project
from api.routers import project
#from api.routers import model
#from api.routers import preprocess_data, optimized_value
#from api.routers import data

app = FastAPI()
app.include_router(user.router)
#app.include_router(intermediate_user_project.router)
app.include_router(project.router)
#app.include_router(model.router)
#app.include_router(preprocess_data.router)
#app.include_router(optimized_value.router)
#app.include_router(data.router)