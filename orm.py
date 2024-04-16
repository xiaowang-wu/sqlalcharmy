from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dbConfig import Student, User
from sqlalchemy.orm import sessionmaker
from dbConfig import engine


session = sessionmaker(engine)()

#t添加数据
# student = Student(name='wyw', age='23', sex='male')
# session.add(student)
# session.commit()

# # 查询数据
# data_list = session.query(Student).all()
# for item in data_list:
#     print(item.name,item.age)

# 查找指定列
# print(session.query(Student.name).all())

# print(session.query(Student).first().name)
 # 筛选

# data_list = session.query(Student).filter(Student.age>25).all()
# print(data_list[0].name)


# 等价
# data_list = session.query(Student.name).filter(Student.age>20,Student.age<25).all()
# print(len(data_list))
# in
# data_list = session.query(Student.name).filter(Student.age.in_([20,25])).all()
# print(data_list)


# data_list = session.query(Student.name).filter(Student.id<10,Student.sex=='M').order_by(Student.age.desc()).all()
# print(data_list)


# LIKE
# data_list = session.query(Student.name).filter(Student.name.like("w%"),Student.id<10).all()
# print(data_list)

# 统计

# data_list = session.query(Student.name).filter(Student.age==23).count()
# print(data_list)

# 修改数据
# data_list = session.query(Student).filter(Student.name=='wyw').update({'age':18})
# session.commit()

# 删除数据 
# session.query(Student).filter(Student.age==809).delete()
# session.commit()
