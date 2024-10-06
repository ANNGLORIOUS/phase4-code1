from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

#Define the hero class that will be used to interact with the database.
class Hero(db.Model):
    __tablename__ = 'heroes'

#create the columns.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

#one-to-many relationship with the Heropower class.
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')


#Define the power class that will interact with the database
class Power(db.Model):
    __tablename__ = 'powers'


#create the columns.
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String(20), nullable=False)

#one-to-many relationship with the Hero class.
    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')


#Define the HeroPower class that will interact with the database.
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'



#create the columns.
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

#relationship
    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

#validate the strength according to strong,weak and average.
@validates('strength')
def validate_strength(self, key, strength):
    if strength not in ['strong', 'weak', 'average']:
        raise ValueError('Not of valid strength')
    return strength

#validate the description must be present and atleast 20 characters long.
@validates('description')
def validate_description(self, key, description):
    if description is None or len(description) < 20:
        raise ValueError('Description must be present and at least 20 characters long.')
    return description




