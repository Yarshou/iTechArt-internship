from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shops'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    address = Column(String(255), nullable=True)
    staff_amount = Column(Integer)


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    sphere = Column(String(255))
    staff_amount = Column(Integer)
    shop_id = Column(Integer, ForeignKey('shops.id'))


class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(String(255), nullable=True)
    price = Column(Integer)
    department_id = Column(Integer, ForeignKey('departments.id'))
