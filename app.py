from bs4 import BeautifulSoup
import requests

class Music:
    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')


    def page(self):
        print(self.soup.prettify())