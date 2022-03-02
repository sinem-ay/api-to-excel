from urllib import response
import requests
import openpyxl
import time

api_url = 'https://jsonplaceholder.typicode.com/users'

def extract_user_details(search_term):

    params = {
        'users': 'id;name;username;email;address'
    }

    response = requests.get(api_url + search_term, params=params)
    response.json()


def write_user_details():
    filename = 'users.xlsx'

    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    wc = ws['A1'] = 'id'

    

    wb.save(filename)

write_user_details()