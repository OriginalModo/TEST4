from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    time_to_cook = Column(Integer)


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    person_name = Column(String)
    products = relationship('OrderProduct', back_populates='order')


class OrderProduct(Base):
    __tablename__ = 'order_products'

    id = Column(Integer, primary_key=True)
    order_id = Column(Integer, ForeignKey('orders.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)

    order = relationship('Order', back_populates='products')