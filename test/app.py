from bs4 import BeautifulSoup
import requests

class Music:
    def __init__(self, url : str):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

    def download_page(self):
       return self.soup.prettify