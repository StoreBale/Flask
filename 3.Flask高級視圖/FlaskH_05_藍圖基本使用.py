from flask import Flask, url_for,render_template
from FlaskH_05.user import user_bp
from FlaskH_05.news import news_bp

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)


@app.route('/')
def hello_world():  # put application's code here
    print(url_for('news.news_list'))
    return render_template('FlaskH_05_index.html')


if __name__ == '__main__':
    app.run()
