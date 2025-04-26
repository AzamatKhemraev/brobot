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
            model="openai/gpt-4o-mini",  # deepseek/deepseek-chat-v3-0324
            messages=[
                {"role": "system", "content": "Ты магистр Йода, твоя задача обучать юнлингов"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        if not response or not response.choices:
            return f"🤖 Не удалось получить ответ от нейросети.\nRaw: {response.model_dump()}"

        content = response.choices[0].message.content
        return content.strip() if content else "🤖 Модель вернула пустой ответ."

    except Exception as e:
        return f"❌ Ошибка при обращении к модели: {e}"
