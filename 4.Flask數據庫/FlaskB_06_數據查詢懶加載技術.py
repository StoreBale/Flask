# encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, Enum, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
    age = Column(Integer, default=0)
    gender = Column(Enum('male', 'female', 'secret'), default='male')


# Base.metadata.drop_all()
# Base.metadata.create_all()

# user1 = User(username = '王一',age=17,gender=('male'))
# user2 = User(username = '趙二',age=33,gender=('male'))
# user3 = User(username = '老三',age=22,gender=('female'))
# user4 = User(username = '黃四',age=17,gender=('secret'))
# user5 = User(username = '張武',age=51,gender=('male'))
#
# session.add_all([user1,user2,user3,user4,user5])
# session.c
