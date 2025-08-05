from telebot.types import Message

from config import DEFAULT_COMMANDS
from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    """
    Выводит описание команд, которые можно использовать в боте.

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
