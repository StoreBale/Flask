from flask import Flask, views, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('login.html')


class LoginView(views.MethodView):
    def __render(self, error=None):
        return render_template('FlaskH_03.html', error=error)

    def get(self, error=None):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'Ting' and password == '1111':
            return '登入成功'
        else:
            return self.__render(error='用戶或密碼錯誤')


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))

if __name__ == '__main__':
    app.run()
