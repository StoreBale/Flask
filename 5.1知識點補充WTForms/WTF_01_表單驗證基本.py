from flask import Flask, request, render_template

from WTF_01_forms import RegistForm, LoginForm, SettingsForm

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/regist/', methods=['GET', 'POST'])
def regist():
    if request.method == 'GET':
        return render_template('WTF_01_regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("WTF_01_login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'


@app.route('/settings/', methods=['GET', 'POST'])
def settings():
    if request.method == 'GET':
        form = SettingsForm(request.form)
        return render_template('WTF_01_settings.html',form=form)
    else:
        form = SettingsForm(request.form)
        pass


if __name__ == '__main__':
    app.run()
