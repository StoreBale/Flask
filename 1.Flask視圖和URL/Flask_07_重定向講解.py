from flask import Flask, request, redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/login/')
def login():
    return '這是登入介面'


@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '個人中心'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
