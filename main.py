from flask import Flask, render_template, url_for, request, redirect
from flaskext.mysql import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'probando_mysql'
mysql = MySQL(app)

@app.route('/')
def mysql():
    return render_template('index.html')

def new_func(app):
    app.run(port=3000,debug=True)

if __name__ == '__main__':
    new_func(app)