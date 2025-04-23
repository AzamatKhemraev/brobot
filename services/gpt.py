import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


async def chat_with_gpt(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # или "gpt-4", если доступен
            messages=[
                {"role": "system", "content": "Ты дружелюбный и остроумный Telegram-бот."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Ошибка при обращении к OpenAI: {e}"
