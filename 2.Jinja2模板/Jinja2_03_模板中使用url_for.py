from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index_03.html')


# {{用來存放變量}}
# {% 用來執行函數或邏輯代碼 %}
@app.route('/acc/login/<id>/')
def login(id):
    return render_template('index_03_login.html')


if __name__ == '__main__':
    app.run()
