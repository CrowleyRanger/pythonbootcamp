import requests
from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

ORIGIN_CITY_IATA = "GRU"

for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] == flight_search.get_destination_code(row["city"])

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"]
    )
    pprint(flight)