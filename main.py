import json
import requests

# Get request and status check
def get_api(url):
    api = requests.get(url)
    def check_status():
        try:
            api.raise_for_status()
        except requests.exceptions.HTTPError as error:
            print(error)

get_api('https://api.coindesk.com/v1/bpi/currentprice.json')

# Dictionary keys - Problem: Does not return anything
"""api = requests.get(url)
    json = api.json()
    json.keys()"""

def get_json(url):
    api = requests.get(url)
    json = api.json()

    def dict_keys():
        print(json.keys())
    return dict_keys

get_json('https://api.coindesk.com/v1/bpi/currentprice.json')

def my_logger(function):
    import logging
    logging.basicConfig(filename='{}.log'.format(function.__name__), level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info('Ran with args:{}, and kwargs: {}'.format(args, kwargs))
        return function(*args, **kwargs)

    return wrapper()

def my_timer(function):
    import time

    def wrapper(*args, **kwargs):
        t1=time.time()
        result=function(*args, **kwargs)
        t2=time.time() - t1
        print('{} ran in: {} sec'.format(function.__name__, t2))
        return result


@my_timer
def get_api(url='https://api.coindesk.com/v1/bpi/currentprice.json'):
    api = requests.get(url)
    json = api.json()
    print(json.keys())

get_api('https://api.coindesk.com/v1/bpi/currentprice.json')