import json

from flask import Flask, render_template
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sqlalchemy as sa
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import config
from models import Base, ProductTypes, ComputerTypes, Laptops, Desktops, Shops, SaleVariants


app = Flask(__name__, template_folder=config.TEMPLATES_DIR, static_folder=config.STATIC_DIR)

# migrate = Migrate(app, db)
engine = sa.create_engine(config.DB_PATH, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


@app.route('/laptops/', methods=['GET'])
def list_laptops():
    session = Session()
    product_types = session.query(ProductTypes).order_by(sa.desc(ProductTypes.raiting)).limit(7).all()
    laptops = session.query(Laptops).all()
    return render_template('list_products.html', product_type='laptops', items=laptops,
                           product_types=product_types, back_link='/laptops/')


@app.route('/desktops/', methods=['GET'])
def list_desktops():
    session = Session()
    product_types = session.query(ProductTypes).order_by(sa.desc(ProductTypes.raiting)).limit(7).all()
    desktops = session.query(Desktops).all()
    return render_template('list_products.html', product_type='desktops', items=desktops,
                           product_types=product_types, back_link='/desktops/')


@app.route('/')
@app.route('/market/')
def list_product_types():
    session = Session()
    product_types = session.query(ProductTypes).order_by(sa.desc(ProductTypes.raiting)).all()
    return render_template('list_product_types.html', items=product_types,
                           back_link='market', sub_link='sub_type')


@app.route('/sub_type/<int:sub_type_id>')
def list_sub_types(sub_type_id):
    entities = {1: ComputerTypes}
    sub_type_object = entities.get(sub_type_id)
    if sub_type_object:
        session = Session()
        sub_product_types = session.query(sub_type_object).order_by(sa.desc(sub_type_object.raiting)).all()
    else:
        sub_product_types = []
    return render_template('list_sub_types.html', items=sub_product_types,
                           back_link='market'.format(sub_type_id))


@app.route('/product_page/<sub_type_name>/<int:product_id>')
def show_product(sub_type_name, product_id):
    session = Session()
    sub_types = {'desktops': Desktops, 'laptops': Laptops}
    sub_type_obj = sub_types.get(sub_type_name)
    if not sub_type_obj:
        pass
    product = session.query(sub_type_obj).filter(sub_type_obj.id == product_id).first()
    if not product:
        pass
    prod_info = json.loads(product.parameters)
    image_link = "/static/{}".format(product.image)

    sale_variants = session.query(SaleVariants).filter(sa.and_(
        SaleVariants.type_id == product.sub_type.type.id,
        SaleVariants.sub_type_id == product.sub_type.id,
        SaleVariants.product_id == product.id,
    )).all()

    if sale_variants:
        all_prices = [variant.price for variant in sale_variants]
        average_price = round(sum(all_prices) / len(all_prices), 2)
    else:
        average_price = '-'
    return render_template("product_page.html", prod_info=prod_info,
                           product=product, image_link=image_link,
                           sale_variants=sale_variants, average_price=average_price)


@app.route('/static/<file_id>')
def return_static_file(file_id):
    return app.send_static_file(file_id)


if __name__ == '__main__':
    Base.metadata.create_all(engine)
    app.run(debug=True, port=5000)


