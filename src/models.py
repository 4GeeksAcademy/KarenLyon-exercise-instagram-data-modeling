import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    username = Column(String(40), index = True)
    firstname = Column(String(40))
    lastname = Column(String(40))
    email = Column(String(40), nullable = False)

class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__= 'comment'

    id = Column(Integer, primary_key = True)
    comment_text = Column(String(40))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship(User)
    post = relationship(Post)

class Followers(Base):
    __tablename__= 'followers'

    id = Column(Integer, primary_key = True)
    user_to_ID = Column(Integer, ForeignKey('user.id'))
    user_from_ID = Column(Integer, ForeignKey('user.id'))
    user_to = relationship(User) 
    user_from = relationship(User)  
    
## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
