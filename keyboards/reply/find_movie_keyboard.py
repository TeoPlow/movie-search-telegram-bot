from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def gen_find_movie_keyboard():
    """
    Создаёт клавиатуру, которая появляется после команды "Поиск фильмов"

    :return: Возвращает объект клавиатуры
    """
    button_1 = KeyboardButton(text="По названию")
    button_2 = KeyboardButton(text="По рейтингу")
    button_3 = KeyboardButton(text="С высоким бюджетом")
    button_4 = KeyboardButton(text="С низким бюджетом")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_4, button_2, button_3, button_1)
    return keyboard
