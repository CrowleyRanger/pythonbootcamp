import requests
from requests.models import Response
from pprint import pprint
from datetime import datetime
from dateutil.relativedelta import relativedelta

TEQUILA_ID = "xpacerangerflightdeals"
TEQUILA_KEY = "mp0LxOo0k5P9lj6n638836qMWtHNsOaA"

date_now = datetime.now()
date_now_formatted = date_now.strftime(f"%d/%m/%Y")

date_future = date_now + relativedelta(months=6)
date_future_formatted = date_future.strftime(f"%d/%m/%Y")

tequila_endpoint = "http://tequila-api.kiwi.com"
tequila_search = "http://tequila-api.kiwi.com/v2/search"

headers = {
    "apikey": TEQUILA_KEY
}

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{tequila_endpoint}/locations/query"

        query = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        city_code = results[0]["code"]
        return city_code

    def check_flights(self, origin_iata_code, destination_iata_code):
        search_endpoint = f"{tequila_endpoint}/v2/search"

        search = {
            "fly_from": origin_iata_code,
            "fly_to": destination_iata_code,
            "date_from": date_now_formatted,
            "date_to": date_future_formatted,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=search_endpoint, headers=headers, params=search)

        try:
            search_data = response.json()["data"][0]
        except IndexError:
            print(f"[-]No one trip flights found for {destination_iata_code}.")

            search["max_stopovers"] = 2
            response = requests.get(url=search_endpoint, headers=headers, params=search)

            try:
                search_data = response.json()["data"][0]
                print("[+]Flight with 1 stop over found!")
            except IndexError:
                print(f"[-]No two trip flights found for {destination_iata_code}.")
                return None

            print(f"[!]Destination: {destination_iata_code}, Price: ${search_data['price']}")