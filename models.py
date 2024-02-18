from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_sqlalchemy import SQLAlchemy

# Initialize SQLAlchemy with the app
db = SQLAlchemy()

# Define models
class Topics(db.Model):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    level = db.Column(db.Integer)
    parent = db.Column(db.Integer, db.ForeignKey('topics.id'))  # Zelf-referentiële ForeignKey
    path = db.Column(db.Text)
    draft = db.Column(db.Text)

    subtopics = db.relationship('Topics', 
                                backref=db.backref('parent_topic', remote_side=[id]),
                                lazy='dynamic',
                                foreign_keys='Topics.parent')

class articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    title = db.Column(db.Text)
    parent = db.Column(db.Integer)
    description = db.Column(db.Text)
    path = db.Column(db.Text)
    keywords = db.Column(db.Text)
    date = db.Column(db.Text)
    date_modified = db.Column(db.Text)
    draft = db.Column(db.Text)
    weight = db.Column(db.Integer)
    author = db.Column(db.Text)
    content = db.Column(db.Text)

class Contributors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description_short = db.Column(db.Text)
    description_long = db.Column(db.Text)
    skills = db.Column(db.Text)
    linkedin = db.Column(db.Text)
    facebook = db.Column(db.Text)
    twitter = db.Column(db.Text)
    email = db.Column(db.Text)
    image = db.Column(db.Text)
    status = db.Column(db.Text)
    path = db.Column(db.Text)
    content = db.Column(db.Text)

class blogs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    description = db.Column(db.Text)
    path = db.Column(db.Text)
    date = db.Column(db.Text)
    date_modified = db.Column(db.Text)
    draft = db.Column(db.Text)
    content = db.Column(db.Text)
