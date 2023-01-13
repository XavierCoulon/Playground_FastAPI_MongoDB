from fastapi import FastAPI
from routes.car import car
from controllers.controllers import repopulate_db, extract_data_from_page

app = FastAPI()
app.include_router(car, prefix="/api/v1")

repopulate_db()
# print(extract_data_from_page("https://www.automobile-propre.com/voitures/peugeot-508-hybrid4/"))
