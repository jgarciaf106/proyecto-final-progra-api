from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
        
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=False, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_admin = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "name": self.name,
            "is_admin": self.is_admin,
            # do not serialize the password, its a security breach
        }
        
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cat_code = db.Column(db.Integer, unique=True, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.cat_code

    def serialize(self):
        return {
            "cat_code": self.cat_code,
            "description": self.description,
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prod_code = db.Column(db.Integer, unique=True, nullable=False)
    cat_code = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(250), unique=False, nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.prod_code

    def serialize(self):
        return {
            "prod_code": self.prod_code,
            "cat_code": self.cat_code,
            "description": self.description,
        }