from telebot.types import Message
import json
from loader import bot
from database.send_message_to_database import send_message_to_database


def movie_info_processing(movie_info: dict):
    """
    Обрабатывает полученную информацию о фильме в приемлемый для вывода вид.

    :param movie_info: Словарь с информацией о фильме
    """
    if movie_info["name"] is None:
        movie_info["name"] = movie_info["alternativeName"]
    if movie_info["description"] is None:
        movie_info["description"] = "Отсутствует"
    if movie_info["rating"]["kp"] == 0:
        movie_info["rating"]["kp"] = "Отсутствует"
    if movie_info["rating"]["imdb"] == 0:
        movie_info["rating"]["imdb"] = "Отсутствует"
    if movie_info["year"] is None:
        movie_info["year"] = "Отсутствует"
    if movie_info["genres"] is None:
        movie_info["genres"] = "Отсутствует"
    elif not movie_info["genres"] is None:
        movie_info["genres"] = ", ".join([x["name"] for x in movie_info["genres"]])
    if movie_info["ageRating"] is None:
        movie_info["ageRating"] = "Отсутствует"
    elif not movie_info["ageRating"] is None:
        movie_info["ageRating"] = f'{movie_info["ageRating"]}+'
    try:
        if movie_info["poster"]["url"] is not None:
            pass
    except Exception:
        movie_info["poster"] = dict()
        movie_info["poster"]["url"] = "Отсутствует"


def print_movie_list(message: Message, found_answer):
    """
    Выводит пользователю информацию о фильме.

    :param message: Класс сообщение, которое бот получил от пользователя.
    :param found_answer: Ответ на запрос request.json(), в котором хранится информация о фильме.
    """
    try:
        movie_count = len(found_answer["docs"])
        if movie_count == 0:
            raise IndexError
        bot.send_message(message.from_user.id, "Вот список фильмов:")
        for elem in range(movie_count):
            movie_info = found_answer["docs"][elem]

            movie_info_processing(movie_info)

            movie_info_text = (
                f'Название: {movie_info["name"]}\n\n'
                f'Описание: {movie_info["description"]}\n\n'
                f'Рейтинг: \n    Кинопоиск - {movie_info["rating"]['kp']},\n    IMDb - {movie_info["rating"]['imdb']}\n\n'
                f'Год производства: {movie_info["year"]}\n\n'
                f'Жанр: {movie_info["genres"]}\n\n'
                f'Возрастной рейтинг: {movie_info["ageRating"]}\n\n'
                f"Постер: {movie_info["poster"]["url"]}"
            )

            bot.send_message(
                message.from_user.id,
                movie_info_text,
            )

            send_message_to_database(
                user_id=message.from_user.id,
                name=message.from_user.full_name,
                movie_info=movie_info_text,
            )
            print(f"DB-LOG: Добавлены в таблицу данные о поиске пользователя '{message.from_user.full_name}'")

    except IndexError:
        bot.send_message(message.from_user.id, "Ничего не нашлось... Попробуйте снова.")
