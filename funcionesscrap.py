import requests
from bs4 import BeautifulSoup

URL = "https://www.pokeguardian.com/"

def scraper_guardian(url=URL):
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")

    enlaces = soup.select("article header h2 a")
    base = "https://www.pokeguardian.com"

    if enlaces:
        href = enlaces[0].get("href")
        if href:
            return base + href

    return None

