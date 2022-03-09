from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/list/')
def article_list():
    return 'article_list'


@app.route('/article/<article_id>/')
def article_detail(article_id):
    return f'你請求的文章是：{article_id}'


@app.route('/article/<path:test>/')
def test_detail(test):
    return f'test_detail: {test}'


@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return f'用戶的個人中心 {user_id}'


@app.route('/<any(blog,user,sss):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return f'博客詳情： {url_path}'
    elif url_path == 'user':
        return f'使用者詳情： {url_path}'
    else:
        return '用戶詳情： %s' % id

@app.route('/d/')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    print(ie)
    return f'查詢字串的方式傳遞的參數 {wd}'
# /d/?wd=xxxx

# import uuid
# print(uuid.uuid4())


if __name__ == '__main__':
    app.run()
