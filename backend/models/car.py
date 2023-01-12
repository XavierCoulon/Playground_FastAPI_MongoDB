from pydantic import BaseModel, Field
from typing import Optional

class Car(BaseModel):
	model: str = Field(min_length=1)
	brand: str = Field(min_length=1)
	motorisation: Optional[str]
	autonomy: Optional[str]
	image_model: Optional[str] = Field(title="URL of an image of the model")
	price: Optional[int]
	image_brand: Optional[str] = Field(title="Logo of the brand (URL")
	rating: Optional[str]

	class Config:
		schema_extra = {
			"example": {
				"model": "BMW",
				"brand": "Série 5 PHEV",
				"motorisation": "Hybride rechargeable",
				"autonomy": "60 à 61 km",
				"image_model": "https://desimages/voiture.jpeg",
				"price": 50000,
				"image_brand": "https://desimages/logo_BMW.jpeg",
				"rating": "4,6"
			}
		}