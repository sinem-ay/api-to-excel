import xlsxwriter
import json
import requests

url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

querystring = {"q": "Warsaw"}

headers = {
    "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
    "X-RapidAPI-Key": "your-key"
}

response = requests.request("GET", url, headers=headers, params=querystring)
json_api = json.loads(response.text)


def float_to_str(json_data: dict):
    if isinstance(json_data, list):
        iterator = enumerate(json_data)
    elif isinstance(json_data, dict):
        iterator = json_data.items()
    else:
        raise TypeError("needs input of list or dict")

    for i, value in iterator:
        if isinstance(value, (list, dict)):
            float_to_str(value)
        elif isinstance(value, float):
            try:
                json_data[i] = str(value)
            except ValueError:
                pass


float_to_str(json_api)

excel_weather = xlsxwriter.Workbook('excel_weather.xlsx')
excel_sheet = excel_weather.add_worksheet()

row = 0
column = 0

for key in json_api.keys():
    row += 1
    excel_sheet.write(row, column, json.dumps(key))
    for item in json_api[key]:
        excel_sheet.write(row, column, json.dumps(item))
        row += 1

excel_weather.close()
