from sqlalchemy import MetaData, Table, String, Integer, Column, Text, DateTime, Boolean, ForeignKey, insert
from database import Base
from datetime import datetime


class Models(Base):
    __tablename__ = 'models'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)


class Brands(Base):
    __tablename__ = 'brands'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)


class Cars(Base):
    __tablename__ = 'cars'
    id = Column(Integer(), primary_key=True)
    name = Column(String(100))
    title = Column(Text)
    yer = Column(Integer())
    price = Column(Integer())
    link = Column(String(200))
    create_on = Column(DateTime(), default=datetime.now)
    brand_id = Column(Integer, ForeignKey('brands.id'))
    model_id = Column(Integer, ForeignKey('models.id'))
