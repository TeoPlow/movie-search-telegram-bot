from sqlalchemy import create_engine, MetaData, Table, insert
from datetime import datetime


def send_message_to_database(user_id: int, name: str, movie_info: str):
    """
    Сохраняет запрос пользователя в базу данных.

    :param user_id: Идентификатор пользователя, который делал запрос. Хранится в message.from_user.id.
    :param name: Имя пользователя, который делал запрос. Хранится в message.from_user.full_name.
    :param movie_info: Вся информация о фильме, который искал пользователь.
    """
    formatted_datetime = datetime.now()
    engine = create_engine("sqlite:///database/database.db")
    metadata = MetaData()
    database = Table("users_request_history", metadata, autoload_with=engine)
    new_data = {
        "user_id": user_id,
        "name": name,
        "date": formatted_datetime,
        "movie_info": movie_info,
    }

    with engine.connect() as connection:
        insert_stmt = insert(database).values(new_data)
        connection.execute(insert_stmt)
        connection.commit()
