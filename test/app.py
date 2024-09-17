import urllib.parse
import tldextract

def detect_site_origin(url):
    # Extraire le domaine et le sous-domaine de l'URL
    parsed_url = urllib.parse.urlparse(url)
    extracted_domain = tldextract.extract(parsed_url.netloc)
    
    # Récupérer le domaine complet (par exemple 'google.com' ou 'wikipedia.org')
    domain = f"{extracted_domain.domain}.{extracted_domain.suffix}"
    
    return domain

# Exemple d'utilisation
url_1 = "https://www.google.com/search?q=python"
url_2 = "https://fr.wikipedia.org/wiki/Python"

print(detect_site_origin(url_1))  # Sortie: google.com
print(detect_site_origin(url_2))  # Sortie: wikipedia.org
