from dotenv import load_dotenv, find_dotenv
import os

if not find_dotenv():
    exit("Переменные окружения не загружены, отсутствует файл .env")
else:
    load_dotenv()

API_KEY = os.getenv("API_KEY")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_URL = "https://api.kinopoisk.dev/v1.4/"
DEFAULT_COMMANDS = (
    ("start", "Запустить поиск фильмов/сериалов"),
    ("help", "Вывести справку"),
)
