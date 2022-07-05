from flask import Flask, g, render_template
import sqlite3
from DBhandler.DBhandler import DBHandler
import os


app = Flask(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))


controller = None

@app.before_request
def before_request():
    #Устанавливаем соединение с БД
    global controller
    controller = DBHandler(get_db())

def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def get_db():
    #Соединение с БД, если оно еще не установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.teardown_appcontext
def close_db(error):
    #Закрываем соединение с БД, если оно было установлено
    if hasattr(g, 'link_db'):
        g.link_db.close()

#базовая страница
@app.route("/")
def index():
    return render_template("index.html")


#Точка входа
if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.run(debug=True)