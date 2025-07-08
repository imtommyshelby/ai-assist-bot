from .transfermarkt import fetch_transfermarkt_news
from .marca import fetch_marca_news
from .ascom import fetch_as_news
from .twitter_live import fetch_tweets


def fetch_all_sources() -> str:
    sources = []

    try:
        news = fetch_transfermarkt_news()
        if isinstance(news, list):
            sources.extend(news)
        else:
            sources.append(news)
    except Exception:
        pass

    try:
        news = fetch_marca_news()
        if isinstance(news, list):
            sources.extend(news)
        else:
            sources.append(news)
    except Exception:
        pass

    try:
        news = fetch_as_news()
        if isinstance(news, list):
            sources.extend(news)
        else:
            sources.append(news)
    except Exception:
        pass

    try:
        news = fetch_tweets()
        if isinstance(news, list):
            sources.extend(news)
        else:
            sources.append(news)
    except Exception:
        pass

    return "\n".join(sources)



def fetch_relevant_news(topic: str) -> str:
    """
    Filters news snippets from all sources based on the topic keyword.

    Returns a string of up to 5 relevant lines. Falls back to general news if nothing matches.
    """
    all_news = fetch_all_sources()
    relevant_news = []

    for line in all_news.splitlines():
        if topic.lower() in line.lower():
            relevant_news.append(line)

    return "\n".join(relevant_news[:5]) if relevant_news else all_news[:500]
