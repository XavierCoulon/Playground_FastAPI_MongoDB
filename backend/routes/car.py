from fastapi import APIRouter, Query, HTTPException, status
from typing import Optional
from models.car import Car
from config.db import db
from schemas.car import serializeDict, serializeList
from bson import ObjectId

car = APIRouter()

@car.get("/")
async def get_all(n: Optional[int] = Query(1000, gt=0), rating: Optional[bool] = Query(None)):
	query ={}
	if rating:
		query["rating"] = { "$ne": "N/A"}
	if n:
		return serializeList(db.cars.find(query).limit(n))
	return serializeList(db.cars.find(query))

@car.get('/{id}')
async def get_one(id):
	try:
		return serializeDict(db.cars.find_one({"_id":ObjectId(id)}))
	except:
		raise raise_not_found_exception()


@car.post("/", status_code=status.HTTP_201_CREATED)
async def create(car: Car):
	db.cars.insert_one(dict(car))
	return {"message": "Creation OK!"}

@car.put("/{id}", status_code=status.HTTP_200_OK)
async def update(id, car:Car):
	try:
		db.cars.find_one_and_update({"_id":ObjectId(id)},{
			"$set":dict(car)
		})
		return serializeDict(db.cars.find_one({"_id":ObjectId(id)}))
	except:
		raise raise_not_found_exception()

@car.delete('/{id}')
async def delete_user(id):
	try:
		return serializeDict(db.cars.find_one_and_delete({"_id":ObjectId(id)}))
	except:
		raise raise_not_found_exception()
	
def raise_not_found_exception():
	return HTTPException(status_code=404, detail="Car not found", headers={"X-Header-Error": "Nothing to be seen at the provided ID"})

	

