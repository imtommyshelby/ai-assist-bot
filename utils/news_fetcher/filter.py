# utils/news_fetcher/filter.py (create this file if it doesn't exist)

from utils.news_fetcher import fetch_all_sources  # your combined sources function

def fetch_relevant_news(topic: str) -> str:
    all_news = fetch_all_sources()  # Returns a big string of headlines
    relevant_lines = []

    for line in all_news.splitlines():
        if topic.lower() in line.lower():
            relevant_lines.append(line.strip())

    if relevant_lines:
        return "\n".join(relevant_lines[:5])  # Limit to 5 top hits
    else:
        return "No recent headlines found related to this topic."
