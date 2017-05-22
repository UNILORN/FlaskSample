from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test')
def yahho():
    return render_template('index.html', message="sdasdosiadapdokasjdoiasjd")


if __name__ == '__main__':
    app.run()
