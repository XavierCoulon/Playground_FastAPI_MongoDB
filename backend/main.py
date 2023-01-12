from fastapi import FastAPI
from routes.car import car

app = FastAPI()
app.include_router(car, prefix="/api/v1")






