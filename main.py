from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def mysql():
    return render_template('index.html')

def new_func(app):
    app.run(port=3000,debug=True)

if __name__ == '__main__':
    new_func(app)