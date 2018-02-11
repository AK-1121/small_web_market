import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ProductTypes(Base):
    __tablename__ = 'product_types'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(120), unique=True, nullable=False)
    table_name = sa.Column(sa.String(120), unique=True, nullable=False)
    raiting = sa.Column(sa.Integer)
    description = sa.Column(sa.String(1200))


class ComputerTypes(Base):
    __tablename__ = 'computer_types'
    id = sa.Column(sa.Integer, primary_key=True)
    type_id = sa.Column(sa.Integer, sa.ForeignKey("product_types.id"), nullable=False)
    name = sa.Column(sa.String(120), unique=True, nullable=False)
    table_name = sa.Column(sa.String(120), unique=True, nullable=False)
    raiting = sa.Column(sa.Integer)
    description = sa.Column(sa.String(1200))

    type = relationship("ProductTypes", backref="computers")


class Laptops(Base):
    __tablename__ = 'laptops'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    sub_type_id = sa.Column(sa.Integer, sa.ForeignKey("computer_types.id"), nullable=False)
    name = sa.Column(sa.String(120), nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    raiting = sa.Column(sa.Float)
    image = sa.Column(sa.String)
    parameters = sa.Column(sa.Text, nullable=False)

    sub_type = relationship("ComputerTypes", backref="laptops")


class Desktops(Base):
    __tablename__ = 'desktops'
    id = sa.Column(sa.Integer, primary_key=True, nullable=False)
    sub_type_id = sa.Column(sa.Integer, sa.ForeignKey("computer_types.id"), nullable=False)
    name = sa.Column(sa.String(120), nullable=False)
    # type_id = sa.Column(sa.Integer, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    raiting = sa.Column(sa.Float)
    image = sa.Column(sa.String(120))
    parameters = sa.Column(sa.Text, nullable=False)

    sub_type = relationship("ComputerTypes", backref="desktops")


class Shops(Base):
    __tablename__ = 'shops'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(240), nullable=False)
    address = sa.Column(sa.String(240), nullable=False)
    raiting = sa.Column(sa.Float)
    self_pickup = sa.Column(sa.Boolean, nullable=False, default=False)
    phone = sa.Column(sa.String(240), nullable=False)
    delivery_conditions = sa.Column(sa.String(240), nullable=False)
    url = sa.Column(sa.String(240))


class SaleVariants(Base):
    __tablename__ = 'sale_variants'
    id = sa.Column(sa.Integer, primary_key=True)
    type_id = sa.Column(sa.Integer, nullable=False)
    sub_type_id = sa.Column(sa.Integer, nullable=False)
    product_id = sa.Column(sa.Integer, nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey("shops.id"), nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    amount = sa.Column(sa.Integer, nullable=False)
    url = sa.Column(sa.String(240), nullable=False)

    shop = relationship("Shops", backref="sale_variant")
