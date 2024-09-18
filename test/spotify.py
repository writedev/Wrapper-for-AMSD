import requests
from bs4 import BeautifulSoup

class Spotify:
    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, "html.parser")

    def get_html(self):
        html = self.soup.prettify()
        return html
    
    def get_song_name(self):
        html = self.soup