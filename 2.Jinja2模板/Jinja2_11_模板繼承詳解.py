from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index_11.html')

@app.route('/list/')
def my_list():
    return render_template('index_11_list.html')
    
if __name__ == '__main__':
    app.run()