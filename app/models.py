from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

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
