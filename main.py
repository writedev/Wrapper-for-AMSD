import requests
from bs4 import BeautifulSoup

reponse = requests.get("https://www.youtube.com/watch?v=d-kRtycneKs")

soup = BeautifulSoup(reponse.text, 'html.parser')

print(soup.prettify())
