from pydantic import BaseModel

class Car(BaseModel):
	model: str
	brand: str
	motorisation: str
	autonomy: str
	image_model: str
	price: int
	image_brand: str
	rating: str