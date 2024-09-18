import requests
from bs4 import BeautifulSoup

# URL de la page que tu veux scrapper (remplace avec la vraie URL)
url = 'https://open.spotify.com/playlist/1u9WM7cJGDxk8sRNl1S7CM?si=6253ef20bb7e49bb'

# Envoyer une requête GET pour récupérer la page HTML
response = requests.get(url)

# Parser le contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver l'élément parent (ajuste la balise et les classes en fonction de ton besoin)
parent_element = soup.find('div', class_='parent-class')

# Vérifier si l'élément parent est trouvé
if parent_element:
    # Trouver le sous-élément à l'intérieur de l'élément parent
    sub_element = parent_element.find('div', class_='encore-text encore-text-body-medium encore-internal-color-text-base btE2c3IKaOXZ4VNAb8WQ standalone-ellipsis-one-line')
    
    # Vérifier si le sous-élément est trouvé et afficher son contenu
    if sub_element:
        print(sub_element.text)
    else:
        print("Le sous-élément n'a pas été trouvé.")
else:
    print("L'élément parent n'a pas été trouvé.")