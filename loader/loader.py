from flask import request, Blueprint, render_template
from loader.utils import store_post_to_json
import os
import logging
from config import UPLOAD_FOLDER


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

@loader_blueprint.route('/post', methods=['post'])
def view_loaded_post():
    content = request.form.get('content')
    picture = request.files.get('picture')
    if not content or not picture:
        return 'Отсутствует часть данных'
    filename = picture.filename
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        path_to_picture = f'{UPLOAD_FOLDER}/{filename}'
        store_post_to_json(content, path_to_picture)
        picture.save(path_to_picture)
        return render_template('post_uploaded.html', content=content, picture=path_to_picture)
    else:
        logging.info('Пост не загружен. Загруженный файл - не картинка (расширение не jpeg, jpg, png)')
        return f'Пост не загружен. Загруженный файл - не картинка (расширение не jpeg, jpg, png)'


@loader_blueprint.route('/post', methods=['get'])
def load_new_post():
    return render_template('post_form.html')
