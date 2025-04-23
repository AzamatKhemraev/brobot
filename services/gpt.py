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
            model="google/gemini-2.5-pro-exp-03-25:free",  # или другую модель
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content if response.choices else None

        if content:
            return content.strip()
        else:
            return "⚠️ Ответ от модели не получен."
    except Exception as e:
        return f"❌ Ошибка при обращении к модели: {e}"
