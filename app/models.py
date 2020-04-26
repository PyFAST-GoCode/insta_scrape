from flask import Flask
from app import app
from flask import render_template
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/insta_scraper"
# app.config['SQLAlCHEMY_TRACK_MODIFICATIONS'] = False

# app = Fask(__name__)
# db = SQLAlchemy(app)

# migrate = Migrate(app, db)

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String())
    text = db.Column(db.String())
    url = db.Column(db.String())


    def __init__(self, state, name):
        self.date = date
        self.text = text
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)

class LocationData(db.Model):
    __tablename__ = 'location_data'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime())
    lat = db.Column(db.String())
    lon = db.Column(db.String())
    city = db.Column(db.String())
    street_address = db.Column(db.String())
    zip = db.Column(db.String())
    location_id = db.Column(db.String())
    post = db.relationship('Post', lazy=True)

    def __init__(self, date, lat, lon, city, street_address, zip, location_id, post):
        self.date = date
        self.text = text
        self.url = url

    def __repr__(self):
        return '<id {}>'.format(self.id)


        # Lat
        # Lon
        # Date -
        # Timestamp -
        # City
        # Street address
        # Zip code
        # Binned Hashtags:
        # 	Activity (hiking or mtbing or ...)
        # 	Trail name
        # 	Restaurant mention (y/n)
        # 	Beverage mention (y/n) - tricky b/c bar/brewerey vs. liquor store vs. brought vs ...
        # 	Hotel (y/n)
        # 	Camping (y/n)
