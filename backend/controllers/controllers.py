import re
from pprint import pprint
from controllers.soup import Soup
from config.constants import URI
from config.db import db
from tqdm import tqdm

def get_links():
	
	soup = Soup(URI).get()
	links = soup.select("div#results_all_vehicles a[href*=voitures]")
	res = [link["href"] for link in links if link["href"].count("/") == 5] 
	return list(set(res))

def extract_data_from_page(url):
	model = brand = motorisation = autonomy = image_model = image_brand = price = rating = "N/A"
	soup = Soup(url).get()
	
	try:	
		model = soup.find_all("h1", itemprop="name")[0].string.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Model is missing on ${url}")
	try:	
		brand = soup.find_all("a", itemprop="brand")[0].string.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Brand is missing on ${url}")
	try:	
		image_model = soup.find_all("img", itemprop="image")[0]["src"]
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Model's image is missing on ${url}")
	try:	
		motorisation = soup.find_all("h5", itemprop="fuelType")[0].string.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Motorisation is missing on ${url}")
	try:	
		autonomy = soup.find_all("h5", text= re.compile("Autonomie"))[0].find_next("span").text.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Autonomy is missing on ${url}")
	try:	
		image_brand = soup.find_all("img", class_="g-width-70x")[0]["src"]
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Brand's image is missing on ${url}")
	try:	
		price = int("".join(filter(str.isdigit, soup.find_all("h5", text="Prix")[0].find_next("span").text)))
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Price is missing on ${url}")
	try:	
		rating = soup.find_all("div", class_="glsr-star-rating glsr-stars")[0].find_next("span").find_next("span").text.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(f"Rating is missing on ${url}")

	return {"model": model, "brand": brand, "motorisation": motorisation, "autonomy": autonomy, "image_model": image_model, "price": price, "image_brand": image_brand, "rating": rating}
	

def extract_all_data():
	return [extract_data_from_page(page) for page in tqdm(get_links())]

def repopulate_db():
	db.cars.delete_many({})
	print("Database deleted...")
	for car in tqdm(extract_all_data()):
		db.cars.insert_one(car)
	print("...then database populated!")

if __name__ == "__main__":
	pprint(extract_data_from_page("https://www.automobile-propre.com/voitures/peugeot-508-hybrid4/"))
	

