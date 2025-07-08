import requests
from bs4 import BeautifulSoup

def fetch_marca_news():
    url = "https://www.marca.com/en/football.html"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    articles = soup.select("div.mod-item")[:3]
    news_list = []

    for article in articles:
        a_tag = article.select_one("a")
        title = a_tag.text.strip()
        link = "https://www.marca.com" + a_tag["href"]
        news_list.append(f"🇪🇸 [{title}]({link}) - Marca")

    return news_list
