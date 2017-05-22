from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test/<name>')
def yahho(name=None):
    return render_template('index.html', message=name)


if __name__ == '__main__':
    app.run()
