import requests
from rich.console import Console
from rich.table import Table

console = Console()

def fetch_api_news():
    try:
        API_KEY = "f990f8a9070c4036b7a10be267872851"  # Get free key from https://newsapi.org
        url = f"https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={API_KEY}"
        
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data["articles"]:
            raise ValueError("No articles in API response")

        headlines = [article["title"] for article in data["articles"][:5]]

        return headlines

    except Exception as e:
        return [f"Error fetching news: {e}"]
