from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = '929526'

# dialect+driver://username:password@host:port/database
DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,
                                                                                        password=PASSWORD,
                                                                                        host=HOSTNAME, port=PORT,
                                                                                        db=DATABASE)

engine = create_engine(DB_URI)
Base = declarative_base(engine)
session = sessionmaker(engine)()

# 重新修改User表，添加了addresses字段，引用了Address表的主键
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,  autoincrement=True)
    name = Column(String(50),primary_key=True,nullable=False)
    fullname = Column(String(50))
    password = Column(String(100))
    # 在ORM层面绑定和`Address`表的关系
    # addresses = relationship("Address", backref="user")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(50), nullable=False)
    # User表的外键，指定外键的时候，是使用的是数据库表的名称，而不是类名
    user_id = Column(String(50), ForeignKey('users.name'))
    # 在ORM层面绑定两者之间的关系，第一个参数是绑定的表的类名，
    # 第二个参数back_populates是通过User反向访问时的字段名称
    user = relationship('User', backref="addresses")

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


Base.metadata.drop_all()
Base.metadata.create_all()

jack = User(name='jack222', fullname='Jack Bean', password='gjffdd')
add1 = Address(email_address='jack@google.com')
add2 = Address(email_address='j25@yahoo.com')
jack.addresses.append(add1)
jack.addresses.append(add2)
# add1.user = jack
# add2.user = jack
session.add(jack)
session.commit()