import re
from pprint import pprint
from controllers.soup import Soup
from config.constants import URI
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
		brand = soup.find_all("a", itemprop="brand")[0].string.strip('\t\r\n').strip()
		motorisation = soup.find_all("h5", itemprop="fuelType")[0].string.strip('\t\r\n').strip()
		autonomy = soup.find_all("h5", text= re.compile("Autonomie"))[0].find_next("span").text.strip('\t\r\n').strip()
		image_model = soup.find_all("img", itemprop="image")[0]["src"]
		image_brand = soup.find_all("img", class_="g-width-70x")[0]["src"]
		price = int("".join(filter(str.isdigit, soup.find_all("h5", text="Prix")[0].find_next("span").text)))
		rating = soup.find_all("div", class_="glsr-star-rating glsr-stars")[0].find_next("span").find_next("span").text.strip('\t\r\n').strip()
	except (IndexError, AttributeError) as e:
		print(e.__str__())
		print(url)

	return {"model": model, "brand": brand, "motorisation": motorisation, "autonomy": autonomy, "image_model": image_model, "price": price, "image_brand": image_brand, "rating": rating}
	

def extract_all_data():
	return [extract_data_from_page(page) for page in tqdm(get_links())]

if __name__ == "__main__":
	pprint(extract_data_from_page("https://www.automobile-propre.com/voitures/bmw-740e-iperformance/"))


