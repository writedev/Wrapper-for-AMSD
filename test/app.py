import urllib.parse

def extract_url_info(url):
    # Parser l'URL
    parsed_url = urllib.parse.urlparse(url)
    
    # Extraire les informations
    scheme = parsed_url.scheme        # Ex: 'http' ou 'https'
    netloc = parsed_url.netloc        # Ex: 'www.example.com'
    path = parsed_url.path            # Le chemin après le domaine
    params = parsed_url.params        # Paramètres s'ils existent dans le chemin
    query = parsed_url.query          # Les requêtes (après ? dans l'URL)
    fragment = parsed_url.fragment    # Fragment après le #
    port = parsed_url.port            # Le port utilisé, si spécifié
    
    # Afficher les informations extraites
    print(f"Scheme: {scheme}")
    print(f"Netloc: {netloc}")
    print(f"Path: {path}")
    print(f"Params: {params}")
    print(f"Query: {query}")
    print(f"Fragment: {fragment}")
    print(f"Port: {port}")
    
    return {
        "scheme": scheme,
        "netloc": netloc,
        "path": path,
        "params": params,
        "query": query,
        "fragment": fragment,
        "port": port
    }

# Exemple d'utilisation
url = "https://music.apple.com/fr/album/x-slide/1761698525?i=1761698526"
info = extract_url_info(url)