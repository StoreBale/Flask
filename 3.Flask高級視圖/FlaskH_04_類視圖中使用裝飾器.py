from functools import wraps

from flask import Flask, render_template, request, views

app = Flask(__name__)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username and username == 'Ting':
            return func(*args, **kwargs)
        else:
            return '請先登入'

    return wrapper


@app.route('/')
def hello_world():  # put application's code here
    return 'hello'


@app.route('/setting/')
@login_required
def settings():
    return '設置介面'


class ProfileView(views.View):
    decorators = [login_required] #裝飾器
    def dispatch_request(self):
        return '這是個人介面'


app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
    app.run()
