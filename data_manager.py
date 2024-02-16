import requests

SHEETY_PRICE_ENDPOINT = "YOUR SHEETY PRICES ENDPOINT"
SHEETY_USER_ENDPOINT = "YOUR SHEETY USERS ENDPOINT"

class DataManager: 
    
    def __init__(self):
        self.destination_data = {}
    
    # This function is used to get the data from the Google Sheet
    def get_destination_data(self):
        response = requests.get(url = SHEETY_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"] 
        return self.destination_data
        
    # This function is used to update the destination codes in the Google Sheet
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url = f"{SHEETY_PRICE_ENDPOINT}/{city['id']}",
                json = new_data
            ) 
            print(response.text)
    
    # This function is used to get the customer emails from the Google Sheet
    def get_customer_emails(self):
        response = requests.get(url = SHEETY_USER_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data

