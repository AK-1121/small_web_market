from sqlalchemy import Column, Integer, Float, String
from test_database import Base


class ComputerProductType(Base):
    id = Column(Integer, primary_key=True)
    product_type = Column(String(120), unique=True, nullable=False)

    def __init__(self, type_id=None, product_type=None):
        self.type_id = type_id
        self.product_type = product_type

    def __repr__(self):
        return "ComputerProductType %r" % self.id


# class Laptops(Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(120), nullable=False)
#     product_type = Column(String(120), nullable=False)
#     price = Column(Float, nullable=False)
#     raiting = Column(Float)
#     image = Column(String)
#
#
# class Desktops(Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String(120), nullable=False)
#     product_type = Column(String(120), nullable=False)
#     price = Column(Float, nullable=False)
#     raiting = Column(Float)
#     image = Column(String)
