import requests
from google_api_handler import result as hobbit_data
from google_api_handler import result2 as war_data

base = "http://127.0.0.1:5000/"

# PUT request from hobbit data
for i in range(len(hobbit_data)):
    response = requests.put(base + "books/id/" + hobbit_data[i]['id'], hobbit_data[i])
    print(response.json())

input("Click to continue testing")
print('\n\n')

# GET request by id
response = requests.get(base + "books/id/DqLPAAAAMAAJ")
print(response.json())

input("Click to continue testing")
print('\n\n')

# GET request by author
response = requests.get(base + "books/authors/Corey Olsen")
print(response.json())

input("Click to continue testing")
print('\n\n')

# GET request - list of books
response = requests.get(base + "books")
print(response.json())

# PUT request from war
for i in range(len(war_data)):
    response = requests.put(base + "books/id/" + war_data[i]['id'], war_data[i])
    print(response.json())

input("Click to continue testing")
print('\n\n')

# GET request - list of books
response = requests.get(base + "books")
print(response.json())
