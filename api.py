import requests
url = "https://dummyjson.com/users"

response = requests.get(url)

if(response.status_code == 200):
    print("api successfully connected")
    data = response.json()
    print(data)
else:
    print("data not found")
