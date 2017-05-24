# coding=utf-8
from flask import Flask, render_template, session
from flask_mysqldb import MySQL

app = Flask(__name__)
mysql = MySQL(app)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


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
def session_test(name):
    session['session'] = name
    return render_template('index.html', message=name)


# session show
@app.route('/session/show')
def session_show_test():
    name = session['session']
    return render_template('index.html', message=u'あなたが設定したセッションは「' + name + u'」です。')


if __name__ == '__main__':
    app.run()
