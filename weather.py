import os
import requests
from rich.console import Console
from rich.panel import Panel
from dotenv import load_dotenv

load_dotenv()

console = Console()

def get_weather(city="Pune"):
    # Get your free API key from https://www.weatherapi.com/
    API_KEY = os.environ.get("WEATHER_API_KEY")
    
    if not API_KEY:
        return {"error": "Missing API key! Get one from: https://www.weatherapi.com/"}

    try:
        url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 403:
            return {"error": "Invalid API key"}
            
        response.raise_for_status()
        data = response.json()
        
        weather_info = {
            "temperature_c": data['current']['temp_c'],
            "condition": data['current']['condition']['text'],
            "humidity": data['current']['humidity'],
            "wind_kph": data['current']['wind_kph'],
            "city": city.title()
        }
        
        return weather_info
        
    except requests.exceptions.RequestException as e:
        return {"error": f"Network error: {e}"}
