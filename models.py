#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
# Imports

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    website = db.Column(db.String(250))
    seeking_talent = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(250))
    shows = db.relationship('Show', backref=db.backref('venue', lazy=True))

    # TODO: implement any missing fields,
    #  as a database migration 
    # using Flask-Migrate
    def __repr__(self):
      return f'<Venue {self.id} name: {self.name}>'

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    genres = db.Column("genres", db.ARRAY(db.String()), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=True)
    seeking_description = db.Column(db.String(120))
    shows = db.relationship('Show', backref=db.backref('artist', lazy=True))
    
    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    def __repr__(self):
      return f'<Artist {self.id} name: {self.name}>'

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
# Association table
class Show(db.Model):
    __tablename__ = 'Show'

    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
      return f'<Show {self.id}, Artist {self.artist_id}, Venue {self.venue_id}>'


