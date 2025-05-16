import requests
from bs4 import BeautifulSoup

def crawl_links(url, depth):
    visited_urls = set()
    print(f"Crawling: {url} at depth: {depth}")
    visited_urls.add(url)
    found_urls = {url}  

    response = requests.get(url, timeout=5)
    response.raise_for_status() 
    soup = BeautifulSoup(response.text, 'html.parser')

    if depth == 0:
        return found_urls

    for link in soup.find_all('a', href=True):
        href = link['href']
        # Construct absolute URL if it's relative
