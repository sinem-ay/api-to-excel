# Tutorial for creating virtual environment:
# https://docs.python.org/3/tutorial/venv.html

# medium.com - Consuming NASA API using Python

# api.nasa.gov - register for API key

# Packages required:
# requests - for making HTTP requests
# pprint - for printing structures of data in a formatted way
# urllib - for handling URLs

from urllib import response
import requests 
from urllib.request import urlretrieve
from pprint import PrettyPrinter

pp = PrettyPrinter()
apiKey = '4Zv1VwyT9RT0mmtMH3afvWDf5x16HzZtKSYDZy8P'

# APOD API - Astronomy picture of the day

def fetchAPOD():
    URL_APOD = "https://api.nasa.gov/planetary/apod"
    date = '2022-03-01'
    params = {
        'api_key': apiKey,
        'date': date,
        'hd': 'True'
    }
    response = requests.get(URL_APOD, params=params).json()
    pp.pprint(response)

fetchAPOD()
