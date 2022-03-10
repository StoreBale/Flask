from flask import Flask, url_for ,redirect

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    # (endpoint,**values)
    a = url_for('my_list', page=1, ccc=888)
    print(a)
    return redirect(a)


@app.route('/12/')
def hello_world2():  # put application's code here
    # (endpoint,**values)
    a = url_for('login', next='/')
    print(a)
    return a


@app.route('/login/')
def login():
    return 'login'


@app.route('/list/<page>/<ccc>')
def my_list(page, ccc):
    return f'my_list {page} {ccc}'


if __name__ == '__main__':
    app.run()
