import os
import requests
from dotenv import find_dotenv, load_dotenv
import random
def res():
    index = random.randint(0,7000)
    Base_URL = "https://space-facts-api.techgenius7777.tech/api/v1/resources/fact?number=1"
    response = requests.get(
        Base_URL
    )
    return response.json()[0]['fact']
