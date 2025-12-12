from collections import defaultdict, deque

# Храним последние 50 сообщений по chat_id
message_history = defaultdict(lambda: deque(maxlen=50))  # 50 последних сообщений на чат


def add_to_history(chat_id: int, user_id: int, display_name: str, role: str, content: str):
    message_history[chat_id].append({
        "user_id": user_id,
        "display_name": display_name,
        "role": role,
        "content": content
    })


def get_history(chat_id: int):
    return list(message_history[chat_id])
