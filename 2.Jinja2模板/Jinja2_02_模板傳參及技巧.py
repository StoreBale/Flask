from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    context = {
        'username': 'King',
        'age': '10',
        'country': 'Tai',
        'teen': {
            'name': 'Aces',
            'height': 174
        }
    }
    return render_template('index_02.html', **context)  # **=dict


if __name__ == '__main__':
    app.run()
