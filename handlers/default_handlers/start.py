from telebot.types import Message
from handlers.custom_handlers.history import get_history_handler
from loader import bot
from keyboards.reply.start_keyboard import gen_start_keyboard

@bot.message_handler(commands=["start"])
def bot_start_handler(message: Message):
    """
    Стартовый обработчик, запускающийся по /start.
    Выводит reply клавиатуру с выбором "Истории" или "Поиском фильмов"

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    text = [
        f"Привет, {message.from_user.full_name}! \nЭто бот для поиска фильмов.\nВыбери функцию."
    ]
    bot.reply_to(message, "\n".join(text), reply_markup=gen_start_keyboard())
