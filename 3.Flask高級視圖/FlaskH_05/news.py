from flask import Blueprint

news_bp = Blueprint('news', __name__)

@news_bp.route('/list/')
def news_list():
    return '新聞列表'

@news_bp.route('/detail/')
def news_detail():
    return '新聞詳情'


