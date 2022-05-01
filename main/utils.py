import json
import os
import logging
from json import JSONDecodeError
from error_app import MyErrorApp
from config import POST_PATH


def load_posts():
    """
    Загружает данные из JSON файла
    """
    path_to_json = os.path.join('data', POST_PATH)
    try:
        with open(path_to_json, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error('JSON файл не найден (модуль utils.py)')
        raise MyErrorApp('JSON файл не найден (модуль utils.py)')

    except JSONDecodeError:
        logging.error('JSON файл не сконвертировался (модуль utils.py)')
        raise MyErrorApp('JSON файл не сконвертировался (модуль utils.py)')


def filtered_posts(s):
    """
    Фильтрует посты по введеному слову
    """
    post_list = load_posts()
    relevant_post_list = []
    for post in post_list:
        if s.lower() in post['content'].lower():
            relevant_post_list.append(post)
    return relevant_post_list
