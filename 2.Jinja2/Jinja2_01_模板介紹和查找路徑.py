from flask import Flask, render_template

app = Flask(__name__,template_folder='/Users/sam/Desktop/test')


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index_01.html')


@app.route('/list/')
def my_list():
    return render_template('posts/list.html')  # 目錄要寫完整


if __name__ == '__main__':
    app.run()
