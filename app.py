import time
from flask import Flask, flash, g, redirect, render_template, request, url_for
import sqlite3
from DBhandler.DBhandler import DBHandler
import os
from models.Dmodel import Dmodel
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'Compas_3D_Files'

app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

dbhandler = None

@app.before_request
def before_request():
    # Устанавливаем соединение с БД
    global dbhandler
    dbhandler = DBHandler(get_db())


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def get_db():
    # Соединение с БД, если оно еще не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


@app.teardown_appcontext
def close_db(error):
    # Закрываем соединение с БД, если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()

# базовая страница
@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        description = request.form['fileDescription']
        file = request.files['fileHandler']
        model = Dmodel(int(time.time()), description)
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], str(model.get_id()) + filename))
            res = model.addItem(dbhandler)
            if res:
                flash("Вы успешно добавили модель!", "success")
                return redirect(url_for('index'))
            else:
                flash("Ошибка при добавлении в БД", "error")


    return render_template("index.html")


# Точка входа
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)
