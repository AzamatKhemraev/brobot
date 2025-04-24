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
            model="deepseek/deepseek-chat-v3-0324:free",  # или другую модель
            messages=[
                {"role": "system", "content": "Ты эрудированный чат бот. Твои ответы должны быть краткими и четкими"},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            top_p=0.95
        )

        if not response or not response.choices:
            return "🤖 Не удалось получить ответ от нейросети."
        
    except Exception as e:
        return f"❌ Ошибка при обращении к модели: {e}"
