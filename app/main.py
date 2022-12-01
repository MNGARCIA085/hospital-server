from fastapi import FastAPI,APIRouter
from auth import routes as auth_routes




# creo las tablas
"""
from database.configuration import engine
from auth import models
models.Base.metadata.create_all(bind=engine)
"""


app = FastAPI()



# rutas
router = APIRouter()

app.include_router(auth_routes.router,tags=['auth'])



@app.get("/")
async def root():
    return {"message": "Hello World"}





