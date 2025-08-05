from sqlalchemy import create_engine, MetaData, Table, select, CursorResult


def get_message_from_database(user_id: int) -> CursorResult[list]:
    """
    Получает данные из базы данных по идентификатору пользователя.

    :param user_id: Идентификатор пользователя, который делал запрос. Хранится в message.from_user.id.
    :return: Возвращает список со всеми запросами пользователя.
    """
    engine = create_engine("sqlite:///database/database.db")
    metadata = MetaData()
    database = Table("users_request_history", metadata, autoload_with=engine)

    with engine.connect() as connection:
        select_author_query = database.select().where(database.c.user_id == user_id)
        return connection.execute(select_author_query)
