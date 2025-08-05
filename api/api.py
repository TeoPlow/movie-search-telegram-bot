from requests import RequestException

from config import API_KEY
from config import BASE_URL
import requests
import re


def get_movies(rating=None, budget=None, limit=None, genre=None, year=None):
    """
    Отправляет запрос к API кинопоиска с переданными параметрами.

    :param rating: Рейтинг фильма
    :param budget: Бюджет фильма
    :param limit: Лимит на вывод фильмов
    :param genre: Жанр фильмов
    :param year: Год выпуска
    :return: Возвращает request.json()
    """

    params = dict()
    if budget is not None:
        params["budget.value"] = budget

    if rating is not None:
        params["rating.imdb"] = rating

    if limit is not None:
        limit_edit = re.search(r"\d+", limit)
        if limit_edit:
            params["limit"] = limit_edit.group()

    if genre is not None:
        params["genres.name"] = genre.lower()

    if year is not None:
        year_edit = re.search(r"\b\d{4}\b", year)
        if year_edit:
            params["year"] = year_edit.group()

    response = requests.get(
        f"{BASE_URL}movie?", params=params, headers={"X-API-KEY": API_KEY}, timeout=10
    )

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        raise RequestException


def get_movies_by_name(name=None, limit=None) -> str:
    """
    Отправляет запрос к API кинопоиска для поиска фильма по названию.

    :param name: Название фильма
    :param limit: Лимит на вывод фильмов.
    :return: Возвращает строку с ответом на запрос request.get().text
    """
    params = dict()
    if name is not None:
        params["query"] = name
    if limit is not None:
        limit_edit = re.search(r"\d+", limit)
        if limit_edit:
            params["limit"] = limit_edit.group()

    response = requests.get(
        f"{BASE_URL}movie/search?",
        params=params,
        headers={"X-API-KEY": API_KEY},
        timeout=10,
    )

    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        raise RequestException