from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():  # put application's code here
    context = {
        'article': 'hello you hello hello good',
        'create_time': datetime(2022, 2, 20, 16, 0, 0),
    }
    return render_template('index_05.html', **context)


@app.template_filter('cut')
def cut(value):
    value = value.replace("hello", " ")
    return value


@app.template_filter('handle_time')
def handle_time(time):
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '剛剛'
        elif 60 <= timestamp < 60 * 60:
            minutes = timestamp / 60
            return '%s分鐘前' % int(minutes)
        elif 60 * 60 <= timestamp < 60 * 60 * 24:
            hours = timestamp / (60 * 60)
            return f'{hours} 小時前'
        elif 60 * 60 * 24 < timestamp < 60 * 60 * 24 * 30:
            days = timestamp / (60 * 60 * 24)
            return f'{int(days)} 天前'
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == '__main__':
    app.run()
