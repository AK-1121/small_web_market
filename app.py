from flask import Flask, render_template, session
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class ComputerProductTypes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(120), unique=True, nullable=False)


class Laptops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    product_type = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    raiting = db.Column(db.Float)
    image = db.Column(db.String)


# insert into desktops values (1, "IBM 280", "laptop", 3381.12, 3.8, "");
class Desktops(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    # type_id = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    raiting = db.Column(db.Float)
    image = db.Column(db.String)


db.create_all()
db.session.commit()


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
    laptops = Laptops.query.all()
    return render_template('list_category.html', product_type='laptops', products=laptops)


@app.route('/desktops/', methods=['GET'])
def list_desktops():
    desktops = Desktops.query.all()
    return render_template('list_category.html', product_type='desktops', products=desktops)


@app.route('/')
def list_index():
    return "Hello world!"


if __name__ == '__main__':
    session['product_types'] = {}
    app.run(debug=True, port=5000)


