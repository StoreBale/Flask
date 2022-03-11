from flask import Blueprint

cms_bp = Blueprint('cms', __name__, subdomain='cms')


# IP地址不能有子域名
# localhost也不能有子域名
@cms_bp.route('/')
def index():
    return 'cms index page'
