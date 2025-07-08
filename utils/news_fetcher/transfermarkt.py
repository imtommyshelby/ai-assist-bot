import requests
from bs4 import BeautifulSoup

def fetch_transfermarkt_news():
    url = "https://www.transfermarkt.com/international-transfers/news"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    articles = soup.select("div.news-content")[:3]
    news_list = []

    for article in articles:
        title = article.select_one("h3").text.strip()
        link = "https://www.transfermarkt.com" + article.select_one("a")["href"]
        news_list.append(f"🔄 [{title}]({link}) - Transfermarkt")

    return news_list
