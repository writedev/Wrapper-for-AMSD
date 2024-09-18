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

        meta_title = self.soup.find('meta', property='og:title')

        if meta_title:
            song_name = meta_title['content']
            return song_name
        else:
            print("Impossible de trouver le nom de la chanson.")
    

    def get_image(self):
        meta_title = self.soup.find('meta', property='og:image')

        if meta_title:
            song_name = meta_title['content']
            return song_name
        else:
            print("Impossible de trouver le nom de la chanson.")





    def get_all(self):
        meta_tags = self.soup.find_all('meta', attrs={'property': True})

# Afficher toutes les propriétés et leur contenu
        for meta in meta_tags:
            property_value = meta.get('property')
            content_value = meta.get('content')
            print(f"property: {property_value}, content: {content_value}")