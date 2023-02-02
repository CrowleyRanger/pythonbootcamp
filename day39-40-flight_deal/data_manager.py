from pprint import pprint
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/23ed44e12fb58ca763b1858ab49312e5/flightDeals/prices"

class DataManager:

    def __init__(self):
        self.cities_dict = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.cities_dict = data["prices"]
        return self.cities_dict