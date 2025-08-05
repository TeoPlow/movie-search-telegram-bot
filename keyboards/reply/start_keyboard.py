from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


def gen_start_keyboard():
    """
    Создаёт клавиатуру, которая появляется после команды /start

    :return: Возвращает объект клавиатуры
    """
    button_1 = KeyboardButton(text="Поиск фильмов🎬")
    button_2 = KeyboardButton(text="История📜")

    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button_1, button_2)
    return keyboard
