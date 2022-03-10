from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', endpoint='index')
def hello_world():  # put application's code here
    print(url_for('end'))
    return 'Hello World!'


def my_list():
    return 'mylist'


app.add_url_rule('/list/', endpoint='end', view_func=my_list)

with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run()
