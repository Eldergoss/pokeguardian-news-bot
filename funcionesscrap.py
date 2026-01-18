import requests
from bs4 import BeautifulSoup

URL = "https://www.pokeguardian.com/"

def scraper_guardian(url=URL):
    """
    Devuelve el enlace del último post en PokéGuardian.
    """
    try:
        respuesta = requests.get(url, timeout=10)
        respuesta.raise_for_status()
    except requests.RequestException as e:
        print(f"Error al acceder a {url}: {e}")
        return None

    soup = BeautifulSoup(respuesta.text, "html.parser")

    # Selección más general de enlaces de posts
    enlaces = soup.select("div.jw-element-news-content article header h2 a")

    if enlaces:
        href = enlaces[0].get("href")
        if href:
            # Asegurarse de que sea URL absoluta
            if href.startswith("http"):
                return href
            else:
                return "https://www.pokeguardian.com" + href

    return None
