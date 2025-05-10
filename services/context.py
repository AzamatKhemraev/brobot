from collections import defaultdict, deque

# Храним сообщения по chat_id
message_history = defaultdict(lambda: deque(maxlen=50))  # 50 последних сообщений на чат


def add_to_history(chat_id: int, role: str, content: str):
    message_history[chat_id].append({"role": role, "content": content})


def get_history(chat_id: int):
    return list(message_history[chat_id])
