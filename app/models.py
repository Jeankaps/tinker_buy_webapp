from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from flask_login import UserMixin
from datetime import datetime

# Create a database object
db = SQLAlchemy()

# Init db and return list of class tables
def init_db(app):
    db.init_app(app)
    # Reflect the existing database schema
    Base = automap_base()
    with app.app_context():
        Base.prepare(db.engine, reflect=True)

        # Access the reflected tables
        User = Base.classes.User 
        Account_Details = Base.classes.Account_Details
        Address = Base.classes.Address
        Card = Base.classes.Card
        Cart = Base.classes.Cart
        Category = Base.classes.Category
        Order_Item = Base.classes.Order_Item
        Preferences = Base.classes.Preferences
        Product = Base.classes.Product
        Report = Base.classes.Report
        Shipment = Base.classes.Shipment
        Transaction = Base.classes.Transaction
 # Return the reflected classes for use elsewhere in the application
    return {
        'User': User,
        'Account_Details': Account_Details,
        'Address': Address,
        'Card': Card,
        'Cart': Cart,
        'Category': Category,
        'Order_Item': Order_Item,
        'Preferences': Preferences,
        'Product': Product,
        'Report': Report,
        'Shipment': Shipment,
        'Transaction': Transaction
    }


# UserMixin is used directly with the reflected User class
class User(UserMixin, db.Model):
    __tablename__ = 'User'  # Set the tablename

    # Define the columns of the User table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(45), unique=True)
    password = db.Column(db.String(260))
    user_type = db.Column(db.String(20))
    registration_date = db.Column(db.DateTime)  
    last_login = db.Column(db.DateTime)         
    user_status = db.Column(db.String(45))

