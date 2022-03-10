from flask import Flask, views, url_for, jsonify, render_template

app = Flask(__name__)


class JSONView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JSONView):
    def get_data(self):
        return {"user": 'Ting', 'password': 'f;lejf2i3nnfqbnq243g;iq3ng3qng;i3bq;q34bg3qbge'}


app.add_url_rule('/list/', view_func=ListView.as_view('list'))


class ADsView(views.View):
    def __init__(self):
        super(ADsView, self).__init__()
        self.context = {
            'ads': '廣告zzz'
        }


class LoginView(ADsView):
    def dispatch_request(self):
        self.context.update({
            'user':'Ting'
        })
        return render_template('FlaskH_02_login.html', **self.context)


class RegistView(ADsView):
    def dispatch_request(self):
        return render_template('FlaskH_02_regist.html', **self.context)


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))


# with app.test_request_context():
#     print(url_for('Mylist'))

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
