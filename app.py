from flask import Flask, render_template
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/local_old.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
engine = sa.create_engine('sqlite:///local.db', echo=True)
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


class ProductTypes(Base):
    __tablename__ = 'product_types'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(120), unique=True, nullable=False)
    raiting = sa.Column(sa.Integer)
    description = sa.Column(sa.String(1200))


class ComputerProductTypes(Base):
    __tablename__ = 'computer_product_types'
    id = sa.Column(sa.Integer, sa.ForeignKey("product_types.id"), primary_key=True)
    name = sa.Column(sa.String(120), unique=True, nullable=False)
    raiting = sa.Column(sa.Integer)
    description = sa.Column(sa.String(1200))


class Laptops(Base):
    __tablename__ = 'laptops'
    item_id = sa.Column(sa.Integer, sa.ForeignKey("computer_product_types.id"), primary_key=True)
    name = sa.Column(sa.String(120), nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    raiting = sa.Column(sa.Float)
    image = sa.Column(sa.String)
    parameters = sa.Column(sa.Text, nullable=False)


class Desktops(Base):
    __tablename__ = 'desktops'
    item_id = sa.Column(sa.Integer, sa.ForeignKey("computer_product_types.id"), primary_key=True)
    name = sa.Column(sa.String(120), nullable=False)
    # type_id = sa.Column(sa.Integer, nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    raiting = sa.Column(sa.Float)
    image = sa.Column(sa.String(120))
    parameters = sa.Column(sa.Text, nullable=False)


class Shops(Base):
    __tablename__ = 'shops'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(240), nullable=False)
    address = sa.Column(sa.String(240), nullable=False)
    raiting = sa.Column(sa.Float)


class SaleVariants(Base):
    __tablename__ = 'sale_variants'
    id = sa.Column(sa.Integer, primary_key=True)
    type_id = sa.Column(sa.Integer, nullable=False)
    sub_type_id = sa.Colu mn(sa.Integer, nullable=False)
    product_id = sa.Column(sa.Integer, nullable=False)
    shop_id = sa.Column(sa.Integer, sa.ForeignKey("shops.id"), nullable=False)
    price = sa.Column(sa.Float, nullable=False)
    amount = sa.Column(sa.Integer, nullable=False)


# db.create_all()
# db.session.commit()


# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
#
#
# @app.route('/products')
# def products_page():
#     # laptop = Laptops('test1', 'laptop', 12.23, 3.8, '1234')
#     db.session.add(laptop)
#     db.session.commit()
#     return render_template('products_list.html')


@app.route('/laptops/', methods=['GET'])
def list_laptops():
    laptops = []
    return render_template('list_category.html', product_type='laptops', products=laptops)


@app.route('/desktops/', methods=['GET'])
def list_desktops():
    session = Session()
    product_types = session.query(ProductTypes).order_by(ProductTypes., reverse=True).limit(7).all()
    # desktops = Desktops.query.all()
    desktops = session.query(Desktops).all()
    print(u"XX24: {}".format(desktops))
    return render_template('list_category.html', product_type='desktops', products=desktops,
                           product_types=product_types)


@app.route('/')
def list_index():
    return "Hello world!"


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5000)


