from flask import Blueprint, render_template

news_bp = Blueprint('news', __name__, url_prefix='/news', template_folder='test')


@news_bp.route('/list/')
def news_list():
    return render_template('test.html')


@news_bp.route('/detail/')
def news_detail():
    return '新聞詳情'
