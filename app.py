from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
import logging
# logging.basicConfig(level=logging.INFO, filename="app.log", format="%(asctime)s : %(levelname)s : %(pathname)s ===> %(message)s")
logging.basicConfig(level=logging.INFO, filename="app.log")


app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

app.run()
