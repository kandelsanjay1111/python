#save html to file
import requests
import json
from bs4 import BeautifulSoup

url = "https://dummyjson.com/users"

params = {}

response = requests.get(url, params=params)

if(response.status_code == 200):
    data = response.json()
    print(response.text)
    with open("data.json", "w") as file:
        json.dump(data,file,indent = 4)
        # f.write(data)
        # f.close()
        # print(data)
else:
    print("data not found")
