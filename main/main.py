from flask import Blueprint, render_template, request
from main.utils import filtered_posts
import logging
from json import JSONDecodeError


main_blueprint = Blueprint('main_blueprint', __name__, template_folder="templates")

@main_blueprint.route('/')
def main_page():
    logging.info('Открываем главную страницу')
    return render_template("index.html")


@main_blueprint.route('/search')
def search_pages():
    s = request.args.get('s')
    logging.info(f'Ищем посты по запросу {s}')
    relevant_post_list = filtered_posts(s)
    if len(relevant_post_list) > 0:
        return render_template("post_list.html", relevant_post_list=relevant_post_list, s=s)
    else:
        logging.info("Постов, удовлетворяющих запросу, не найдено")
        return f"Постов, удовлетворяющих запросу, не найдено"



