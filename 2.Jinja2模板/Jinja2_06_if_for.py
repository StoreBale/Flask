from flask import Flask, render_template

app = Flask(__name__)


# @app.route('/')
# def index():  # put application's code here
#     context = {
#         'username': 'abc',
#         'age': 18,
#     }
#     return render_template('index_06.html', **context)

@app.route('/')
def index():
    context = {
        'users': ['z1', 'z2', 'z3'],
        'person': {
            'name': 'King',
            'age': 19,
            'country': 'Tai'
        }
    }
    return render_template('index_06.html', **context)


if __name__ == '__main__':
    app.run()
