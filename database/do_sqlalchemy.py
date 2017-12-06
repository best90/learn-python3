#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column,String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/test')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='2', name='Bob')
session.add(new_user)
session.commit()
session.close()

session = DBSession()
# 创建Query查询，filter是where条件，
# 最后调用one()返回唯一行，如果调用all()则返回所有行
user = session.query(User).filter(User.id=='2').one()
print('type:',type(user))
print('name:', user.name)
session.close()