import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


async def chat_with_gpt(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="deepseek/deepseek-r1:free",  # или другую модель
            messages=[
                {"role": "system", "content": "Ты дружелюбный и немного дерзкий Telegram-бот Bro. Отвечай с юмором и по делу."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Ошибка при обращении к модели: {e}"
