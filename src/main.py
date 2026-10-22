import os
from dotenv import load_dotenv

# Сначала загружаем переменные из файла .env
load_dotenv()

def print_author():
    # Теперь переменная AUTHOR доступна через os.getenv()
    author = os.getenv("AUTHOR")
    print(f"Автор проекта: {author}")

# Для проверки на своем компьютере оставь эту строку:
print_author()
