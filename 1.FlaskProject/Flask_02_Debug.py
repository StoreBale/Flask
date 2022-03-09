from flask import Flask

app = Flask(__name__)


# app.config.update(DEBUG=True)
# print(isinstance(app.config,dict))

@app.route('/')
def hello_world():  # put application's code here
    a = 1
    b = 0
    print('hey the si')
    # c = a / b
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
