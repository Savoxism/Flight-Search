import requests
import os

BEARER = os.getenv("YOUR SHEETY BEARER TOKEN")
USERNAME = os.getenv("YOUR SHEETY USERNAME")

#This function adds the user (customers) details to the Google Sheet
def post_new_row(first_name, last_name, email):
    SHEETY_USER_ENDPOINT = "YOUR SHEETY USERS ENDPOINT"
    headers = {
        "Authorization": f"Bearer {BEARER}",
        "Content-Type": "application/json",
    }
    body = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email,
        }
    }

    response = requests.post(url=SHEETY_USER_ENDPOINT, headers=headers, json=body)
    response.raise_for_status()
    # print(response.text)