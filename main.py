from loader import bot
from utils.set_bot_commands import set_default_commands
import handlers
from database.create_database import create_database


if __name__ == "__main__":
    set_default_commands(bot)
    create_database()
    print("LOG: Бот запущен")
    bot.infinity_polling()
