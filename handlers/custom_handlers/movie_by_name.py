from requests import RequestException
from telebot.types import Message, ReplyKeyboardRemove
from api.api import get_movies_by_name
from utils.print_movie_list import print_movie_list
from loader import bot

@bot.message_handler(func=lambda message: message.text == "По названию")
def search_movie_by_name(message: Message):
    """
    Функция поиска по имени, которая уточняет у пользователя название фильма и лимит выводимых фильмов.
    Далее она передаёт всё в функцию print_movie_list(), которая печатает ответ.

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    user_data = dict()
    bot.send_message(
        message.from_user.id,
        f"Начинаем поиск {message.text.lower()}. \n\nКак называется фильм?",
        reply_markup=ReplyKeyboardRemove()
    )

    def get_movie_name(next_message: Message):
        """Уточняет имя фильма"""
        nonlocal user_data
        user_data["name"] = next_message.text
        bot.send_message(
            next_message.chat.id, "Спасибо! Теперь введите кол-во выводимых фильмов."
        )
        bot.register_next_step_handler(next_message, get_movie_limit)

    def get_movie_limit(next_message: Message):
        """Уточняет лимит выводимых фильмов и передаёт все в print_movie_list(), которая печатает ответ."""
        nonlocal user_data
        user_data["limit"] = next_message.text
        bot.send_message(next_message.chat.id, "Спасибо!")

        try:
            print_movie_list(
                message,
                get_movies_by_name(limit=user_data["limit"], name=user_data["name"]),
            )
        except RequestException:
            bot.send_message(
                next_message.chat.id, "Простите, сервер не отвечает. Попробуйте заново."
            )

    bot.register_next_step_handler(message, get_movie_name)
