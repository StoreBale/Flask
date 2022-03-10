from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():  # put application's code here
    return render_template('index_07.html')

if __name__ == '__main__':
    app.run()