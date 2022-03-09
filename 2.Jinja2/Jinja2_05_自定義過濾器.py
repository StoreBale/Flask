from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():  # put application's code here
    context = {
        'article': 'hello you hello hello good',
    }
    return render_template('index_05.html', **context)


@app.template_filter('cut')
def cut(value):
    value = value.replace("hello", " ")
    return value


if __name__ == '__main__':
    app.run()
