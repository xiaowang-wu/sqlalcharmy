from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from dbConfig import engine
base = declarative_base()

class Author(base):
    __tablename__='authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class Book(base):
    __tablename__='books'
    id = Column(Integer, primary_key=True)
    tittle = Column(String(20))
    author_id = Column(Integer,ForeignKey('authors.id'))
    author= relationship(Author)

# base.metadata.create_all(engine)

session = sessionmaker(engine)()

books = session.query(Book).options(selectinload(Book.author)).all()
print(books)

# 1V1
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     profile_id = Column(Integer, ForeignKey("profiles.id"))
#     profile = relationship("Profile", back_populates="user", uselist=False)

# class Profile(Base):
#     __tablename__ = "profiles"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="profile", uselist=False)
#   query = session.query(User).options(joinedload("profile"))

# 1Vn
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     orders = relationship("Order", back_populates="user")

# class Order(Base):
#     __tablename__ = "orders"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("users.id"))
#     user = relationship("User", back_populates="orders")

# query = session.query(User).options(joinedload("orders"))


