# encoding: utf-8
from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref

# 在Python3中才有这个enum模块，在python2中没有

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '929526'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4".format(username=USERNAME,
                                                                                           password=PASSWORD,
                                                                                           host=HOSTNAME, port=PORT,
                                                                                           db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)
    uid = Column(Integer,ForeignKey("user.id"))

    author = relationship("User",backref=backref("articles"))
    # __mapper_args__ = {
    #     "order_by": create_time.desc,
    # }

    def __repr__(self):
        return "<Article (title:%s,DateTime:%s)>" % (self.title, self.create_time)


# Base.metadata.drop_all()
# Base.metadata.create_all()
#
# article1 = Article(title='fir')
# user = User(username='Zscing')
# user.articles = [article1]
# session.add(user)
# session.commit()
#
# import time
# time.sleep(2)
#
# article2 = Article(title='sec')
# user.articles.append(article2)
# session.commit()

# order＿by 小到大 正序排序
article = session.query(Article).order_by('create_time').all()
print(article)

# desc() 大到小 倒序排序
# article = session.query(Article).order_by(Article.create_time.desc()).all()
# print(article)
