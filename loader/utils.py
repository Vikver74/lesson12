import json
from json import JSONDecodeError
import os
import logging
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
            logging.error('JSON файл не найден (модуль /loader/utils.py)')
            raise MyErrorApp('JSON файл не найден (модуль /loader/utils.py)')

        except JSONDecodeError:
            logging.error('JSON файл не сконвертировался (модуль /loader/utils.py)')
            raise MyErrorApp('JSON файл не сконвертировался (модуль /loader/utils.py)')


def store_post_to_json(content, path_to_picture):
    post_list = load_posts()
    new_post = {"pic": path_to_picture,
                "content": content}
    post_list.append(new_post)
    path_to_json = os.path.join('data', POST_PATH)
    try:
        with open(path_to_json, 'w', encoding='utf-8') as file:
            json.dump(post_list, file, ensure_ascii=False)
            logging.info('Пост добавлен успешно! (модуль /loader/utils.py)')

    except FileNotFoundError:
        logging.error('JSON файл не найден (модуль /loader/utils.py)')
        raise MyErrorApp('JSON файл не найден (модуль /loader/utils.py)')

    except JSONDecodeError:
        logging.error('Ошибка добавление записи в JSON (модуль /loader/utils.py)')
        raise MyErrorApp('Ошибка добавление записи в JSON  (модуль /loader/utils.py)')
