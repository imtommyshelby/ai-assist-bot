# utils/news_fetcher/twitter_live.py

import os
import requests

def fetch_tweets():
    bearer = os.getenv("TWITTER_BEARER_TOKEN")
    headers = {"Authorization": f"Bearer {bearer}"}

    query = "from:liveherewego_ -is:retweet"
    url = f"https://api.twitter.com/2/tweets/search/recent?query={query}&max_results=5&tweet.fields=created_at,text"

    resp = requests.get(url, headers=headers)
    data = resp.json()

    tweets = [f"- {tweet['text']}" for tweet in data.get("data", [])]
    return "\n".join(tweets) if tweets else "No recent tweets found."
