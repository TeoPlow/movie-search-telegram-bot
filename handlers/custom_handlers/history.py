from telebot.types import Message
from database.get_message_from_database import get_message_from_database
from loader import bot

@bot.message_handler(func=lambda message: message.text == "История📜")
def get_history_handler(message: Message):
    """
    Выводит историю запросов пользователю.

    :param message: Класс сообщение, которое бот получил от пользователя.
    """
    bot.send_message(
        message.from_user.id,
        "Вывожу тебе историю запросов!",
    )
    all_messages = get_message_from_database(user_id=message.from_user.id)
    print(f"DB-LOG: Данные о поиске пользователя '{message.from_user.full_name}' взяты из таблицы")
    for elem in all_messages:
        date = elem[3].strftime("%Y-%m-%d %H:%M:%S")
        print(f"History-LOG: Вывел историю запросов пользователя '{message.from_user.full_name}' по времени {date}")
        movie_info = elem[4]
        bot.send_message(
            message.from_user.id,
            f"{date}\n\n{movie_info}",
        )
