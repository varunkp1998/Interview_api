import aiohttp

JOKE_API_URL = "https://v2.jokeapi.dev/joke/Any"

async def fetch_jokes():
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{JOKE_API_URL}?amount=100") as response:
            if response.status == 200:
                data = await response.json()
                return data["jokes"]
            return []
