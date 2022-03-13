import pandas as pd
import requests

# Api for London weather
url = "https://weatherdbi.herokuapp.com/data/weather/london"
r = requests.get(url)
print(r)
# response 200 - success

json = r.json()
# print(json.keys())
# dict_keys(['region', 'currentConditions', 'next_days', 'contact_author', 'data_source'])
print(type(json['currentConditions'])) 
# dict, which means can be transformed into dataframe

weather = pd.DataFrame(json['currentConditions'])
print(weather)
# Current condition of weather in London in dataframe








