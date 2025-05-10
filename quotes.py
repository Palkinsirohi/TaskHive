import asyncio
import aiohttp
from rich.console import Console
from rich.panel import Panel
import random

console = Console()

services = [
    {
        "url": "https://api.quotable.io/random",
        "parse": lambda r: (r["content"], r["author"])
    },
    {
        "url": "https://zenquotes.io/api/random",
        "parse": lambda r: (r[0]["q"], r[0]["a"])
    },
    {
        "url": "https://stoic-quotes.com/api/quote",
        "parse": lambda r: (r["text"], r["author"])
    }
]

local_fallback = [
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Debugging is twice as hard as writing the code in the first place.", "Brian Kernighan")
]

async def fetch_quote(session, service):
    try:
        async with session.get(service["url"], timeout=3) as response:
            json_response = await response.json()
            return service["parse"](json_response)
    except:
        return None

async def get_quote_async():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_quote(session, service) for service in services]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        for result in results:
            if result:
                return result
    # If all fail, return local fallback
    return random.choice(local_fallback)

def get_quote():
    quote, author = asyncio.run(get_quote_async())
    return quote, author

# Removed console.print(get_quote())
