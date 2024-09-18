import requests
from bs4 import BeautifulSoup

class Playist:
    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_music(self):
        