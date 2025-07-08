import requests
from bs4 import BeautifulSoup

def fetch_as_news():
    url = "https://en.as.com/soccer/"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")

    articles = soup.select("article")[:3]
    news_list = []

    for article in articles:
        a_tag = article.select_one("a")
        title = a_tag["title"].strip()
        link = "https://en.as.com" + a_tag["href"]
        news_list.append(f"📢 [{title}]({link}) - AS.com")

    return news_list
