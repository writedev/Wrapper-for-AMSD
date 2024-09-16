from bs4 import BeautifulSoup
import requests

class Music:
    def __init__(self, url):
        self.response = requests.get(url)
        self.soup = BeautifulSoup(self.response.text, 'html.parser')


    def page(self, security_mode=False):
        print(self.soup.prettify())
        if security_mode == False:
            print("le mode securite est desactiver")

        elif security_mode == True:
            print("le mode securite est activer")