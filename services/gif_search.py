import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()
TENOR_API_KEY = os.getenv("TENOR_API_KEY")

if not TENOR_API_KEY:
    raise ValueError("❌ TENOR_API_KEY не найден в .env")


async def get_random_gif_url() -> str | None:
    url = "https://tenor.googleapis.com/v2/random"
    params = {
        "key": TENOR_API_KEY,
        "limit": 1,
        "media_filter": "minimal"
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as resp:
            if resp.status != 200:
                print(f"[ERROR] Tenor API status: {resp.status}")
                return None

            data = await resp.json()
            results = data.get("results")
            if results:
                gif_data = results[0].get("media_formats", {}).get("gif", {})
                return gif_data.get("url")
            return None
