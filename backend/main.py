from tqdm import tqdm
from fastapi import FastAPI
from controllers.controllers import extract_all_data
from routes.car import car
from config.db import db

app = FastAPI()
app.include_router(car, prefix="/api/v1")

def repopulate_db():
	db.cars.delete_many({})
	print("Database deleted...")
	for car in tqdm(extract_all_data()):
		db.cars.insert_one(car)
	print("...then database populated!")




