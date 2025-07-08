from .transfermarkt import fetch_transfermarkt_news
from .marca import fetch_marca_news
from .ascom import fetch_as_news
from .twitter_live import fetch_tweets

def fetch_all_sources():
    news = []
    try: news.extend(fetch_transfermarkt_news())
    except: news.append("❌ Transfermarkt failed.")
    
    try: news.extend(fetch_marca_news())
    except: news.append("❌ Marca failed.")
    
    try: news.extend(fetch_as_news())
    except: news.append("❌ AS.com failed.")
    
    try: news.extend(fetch_tweets())
    except: news.append("❌ X.com fetch failed.")
    
    return "\n".join(news)
