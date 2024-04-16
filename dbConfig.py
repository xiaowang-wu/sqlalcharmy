from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

 # 创建数据库引擎
info='mysql+pymysql://debian-sys-maint:LB4ShZywAS5VDjWW@localhost/mydb'
engine = create_engine(info)


Base = declarative_base()

class User(Base):
    # 表的名字
    __tablename__ = 'users'
    
    # 表的字段
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
 

class Student(Base):
    __tablename__="student"
    id = Column(Integer,primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    sex =Column(String(10))

# 创建表
# Base.metadata.create_all(engine)



