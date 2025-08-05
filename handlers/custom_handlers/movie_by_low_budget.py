from requests import RequestException
from telebot.types import Message, ReplyKeyboardRemove
from api.api import get_movies
from utils.print_movie_list import print_movie_list
from loader import bot


@bot.message_handler(func=lambda message: message.text == "С низким бюджетом")
def search_movie_by_low_budget(message: Message):
    """
    Функция поиска с низким бюджетом, которая уточняет у пользователя рейтинг фильма, его жанр и лимит выводимых фильмов.
    Далее она передаёт всё в функцию print_movie_list(), которая печатает ответ.

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    user_data = dict()
    bot.send_message(
        message.from_user.id,
        f"Начинаем поиск фильмов с низким бюджетом.\n\nКакой рейтинг у фильмов? (Например, 8-10)",
        reply_markup=ReplyKeyboardRemove()
    )

    def get_movie_rating(next_message: Message):
        nonlocal user_data
        user_data["rating"] = next_message.text
        bot.send_message(next_message.chat.id, "Спасибо! Теперь введите жанр фильма.")
        bot.register_next_step_handler(next_message, get_movie_genre)

    def get_movie_genre(next_message: Message):
        nonlocal user_data
        user_data["genre"] = next_message.text
        bot.send_message(
            next_message.chat.id, "Спасибо! Теперь введите кол-во выводимых фильмов."
        )
        bot.register_next_step_handler(next_message, get_movie_limit)

    def get_movie_limit(next_message: Message):
        nonlocal user_data
        user_data["limit"] = next_message.text

        try:
            print_movie_list(
                message,
                get_movies(
                    budget="0-100000", # В долларах
                    limit=user_data["limit"],
                    rating=user_data["rating"],
                    genre=user_data["genre"],
                ),
            )
        except RequestException:
            bot.send_message(
                next_message.chat.id, "Простите, сервер не отвечает. Попробуйте заново."
            )

    bot.register_next_step_handler(message, get_movie_rating)
