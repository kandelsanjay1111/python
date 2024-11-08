#save html to file
import requests
import json
from bs4 import BeautifulSoup

url = "https://dummyjson.com/users"

response = requests.get(url)

if(response.status_code == 200):
    data = response.json()
    with open("data.json", "w") as f:
        json.dump(data,f,indent = 4)
        # f.write(data)
        # f.close()
        # print(data)
else:
    print("data not found")
