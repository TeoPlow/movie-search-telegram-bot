from telebot.types import Message, ReplyKeyboardRemove
from loader import bot
from keyboards.reply.find_movie_keyboard import gen_find_movie_keyboard
from handlers.custom_handlers.movie_by_name import search_movie_by_name
from handlers.custom_handlers.movie_by_rating import search_movie_by_rating


@bot.message_handler(func=lambda message: message.text == "Поиск фильмов🎬")
def movie_search_handler(message: Message):
    """
    Запускает поиск фильмов.

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    bot.send_message(
        message.from_user.id,
        "Приступим к поиску фильмов!",
        reply_markup=gen_find_movie_keyboard(),
    )
