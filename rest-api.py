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
import json
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
response.json()

# POST

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
headers =  {"Content-Type":"application/json"}
response = requests.post(api_url, data=json.dumps(todo), headers=headers)
response.json()

# PUT

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
response.json()

# PATCH

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"title": "Mow lawn"}
response = requests.patch(api_url, json=todo)
response.json()