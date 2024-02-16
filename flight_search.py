import requests
from flight_data import FlightData
# from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "YOUR API KEY"

class FlightSearch:
     
    def __init__(self):
        self.city_codes = []
        
    # This function is used to get the destination codes from the Tequila API
    def get_destination_codes(self, city_names):
        print("get_destination_codes triggered")
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        for city in city_names:
            query = {"term": city, "location_types": "city"}
            response = requests.get(url = location_endpoint, headers = headers, params = query)
            results = response.json()["locations"]
            code = results[0]["code"]
            self.city_codes.append(code)    
        return self.city_codes 
    
    # This function is used to check the flights from the Tequila API
    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {"apikey": TEQUILA_API_KEY}
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7, #minimum nights to stay
            "nights_in_dst_to": 30, #maximum nights to stay
            "flight_type": "round",
            "one_for_city": 1, #cheapest flight for each city
            "max_stopovers": 0, #direct flight
            "curr": "USD" #currency
        }
        response = requests.get(
            url=f"{TEQUILA_ENDPOINT}/v2/search",
            headers=headers,
            params=query,
        )        
        try:
            data = response.json()["data"][0]
        except IndexError:
            query["max_stopovers"] = 1
            response = requests.get(
                url=f"{TEQUILA_ENDPOINT}/v2/search",
                headers=headers,
                params=query,
            )
            try:
                data = response.json()["data"][0]
                # pprint(data)
            except IndexError:
                return None
            else:
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][0]["cityTo"],
                    destination_airport=data["route"][0]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs = 1,
                    via_city=data["route"][0]["cityTo"],
                )
                print(f"{destination_city_code}: ${data['price']}")
                return flight_data  
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0],
            )
            print(f"{destination_city_code}: ${data['price']}")
            return flight_data