from bs4 import BeautifulSoup
import requests

url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)
html_content = req.content
soup = BeautifulSoup(html_content, "html.parser")
paragraphs = soup.find_all("p")
for line in paragraphs:
    print(line)