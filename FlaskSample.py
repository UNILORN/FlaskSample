# coding=utf-8
from flask import Flask, render_template, session

app = Flask(__name__)


# ルーティングと表示
@app.route('/')
def hello_world():
    return 'Hello World!'


# 値渡し HTMLテンプレート
@app.route('/test/<name>')
def html_test(name=None):
    return render_template('index.html', message=name)


# session
@app.route('/session/<name>')
def session_test(name=None):
    session['session'] = name
    return render_template('index.html', message=name)


# session show
@app.route('/session/show')
def sessionshow_test():
    name = session['session']
    return render_template('index.html', message=name)


if __name__ == '__main__':
    app.run()
