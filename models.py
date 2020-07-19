import os 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer
import json
from flask_migrate import Migrate


database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

def setup_dp(app):
    app.config["SQLALCHEMY_DATABASR_URI"] = database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app 
    db.init_app(app)
    db.create_all()

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(80))
    name = db.Column(db.String(80))
    description = db.Column(db.String(120))
    students = db.relationship('Student', backref='subjects', lazy=True)

    def __repr__(self):
        return f'<subjects{self.id}{self.code}{self.name}{self.description}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



class Student(db.Model): 
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)
    gender = db.Column(db.String)
    sub_id = db.Column(db.Integer, db.ForeignKey('subjects.id'), nullable=False)

    def __repr__(self):
        return f'<students{self.id}{self.name}{self.age}{self.gender}{self.sub_id}'

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()



