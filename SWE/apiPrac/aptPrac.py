import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())
base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def articalSearch():
    quary_perameters = {
        "api-key": os.getenv("NYT_KEY"),
        "q":"Apple" 
    }
    responce = requests.get(
        base_url,
        params=quary_perameters,
    )
    headlines = []
    snippets = []
    articals = responce.json()["response"]["docs"]
    for article in articals:
        headlines.append[article["headline"]["main"]]
        snippets.append(article["snippet"])

    return headlines, snippets



# most api is REST -> representation state transfer
# A set of rules the api follow
# This is doen to keep a server restfull
# The rules are the API. 
# API is what are the possible responce and what are are the possible requests 
# It is statesless. It does not remember.
# I saves server space, and it does less work. 