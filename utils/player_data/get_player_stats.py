import requests
from bs4 import BeautifulSoup

def fetch_player_stats(player_name: str) -> str:
    query = player_name.replace(" ", "+")
    search_url = f"https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query={query}"
    headers = { "User-Agent": "Mozilla/5.0" }

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    try:
        profile_link = soup.select_one("a.tm-quicksearch-link").get("href")
        full_url = "https://www.transfermarkt.com" + profile_link
    except AttributeError:
        return f"❌ No player profile found for **{player_name}** on Transfermarkt."

    profile_page = requests.get(full_url, headers=headers)
    soup = BeautifulSoup(profile_page.text, "html.parser")

    try:
        stats_section = soup.select_one("div.dataZusatzbox").text.strip()
        return f"📊 Transfermarkt Stats for **{player_name}**:\n{stats_section}"
    except Exception:
        return f"⚠️ Could not extract detailed stats for **{player_name}**, but profile exists here: {full_url}"
