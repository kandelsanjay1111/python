import requests
import bs4

url = "https://webscraper.io/test-sites/e-commerce/allinone"
html_response = requests.get(url)
soup = bs4.BeautifulSoup(html_response.text,"html.parser")
print(soup.html)