from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/profile/')
def profile():
    return '個人中心'


@user_bp.route('/setting/')
def setting():
    return '個人設置'
