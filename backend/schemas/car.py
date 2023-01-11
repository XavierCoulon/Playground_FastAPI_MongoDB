def carEntity(item) -> dict:
	return {
		"id": str(item(["_id"])),
		"model": item["model"],
		"brand": item["brand"],
		"motorisation": item["motorisation"],
		"autonomy": item["autonomy"],
		"image_model": item["image_model"],
		"image_brand": item["image_brand"],
		"price": item["price"],
		"rating": item["rating"],
	}


def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]

