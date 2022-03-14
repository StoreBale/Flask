# coding = utf-8
from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
# 進入之前資料庫一定要先創建完成
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '929526'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME,
                                                                                        port=PORT,
                                                                                        db=DATABASE)
engine = create_engine(DB_URI)

# 判斷是否連接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())


# class Person(object):
#     name = 'xx'
#     age = 18
#     country = 'xx'

# p = Person('xx',xx)
# p.save()
#
