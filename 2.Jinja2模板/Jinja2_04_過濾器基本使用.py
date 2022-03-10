from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    context = {
        'position': '-9',
        'sign': '<script>alert("hello")</script>',
        'persons': ['data', 'sex', 'BMI']
    }
    return render_template('index_04.html', **context)


if __name__ == '__main__':
    app.run()
