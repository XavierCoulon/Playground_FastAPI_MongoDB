from fastapi import APIRouter
from models.car import Car
from config.db import db
from schemas.car import serializeDict, serializeList
from bson import ObjectId

car = APIRouter()

@car.get("/")
async def get_all():
	return serializeList(db.cars.find())

@car.get('/{id}')
async def get_one(id):
    return serializeDict(db.cars.find_one({"_id":ObjectId(id)}))

@car.post("/")
async def create(car: Car):
	db.cars.insert_one(dict(car))
	return {"message": "Creation OK!"}

@car.put("/{id}")
async def update(id, car:Car):
	db.cars.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(car)
    })
	return serializeDict(db.cars.find_one({"_id":ObjectId(id)}))

@car.delete('/{id}')
async def delete_user(id,car: Car):
    return serializeDict(db.cars.find_one_and_delete({"_id":ObjectId(id)}))
	


	

