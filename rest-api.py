# https://realpython.com/api-integration-in-python/
# Tutorial - Python and REST APIs: Interacting with Web Services

# REST - representational state transfer

# HTTP Methods:
# GET - retrieve an existing resource
# POST - create a new resource
# PUT - update an existing resource
# PATCH - partially update an existing resource
# DELETE - delete a resource

from urllib import response
import requests
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()
