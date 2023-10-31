from flask import Flask, render_template, url_for, request, redirect
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'probando_mysql'
mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def mysql():
    return render_template('index.html')

def new_func(app):
    app.run()

if __name__ == '__main__':
    new_func(app)