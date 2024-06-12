from sqlalchemy import Column, Integer, String, create_engine
from lute.db import db
from flask_login import UserMixin

# Define the AuthUser model
class AuthUser(db.Model,UserMixin):
    __tablename__ = 'auth_user'
    
    id = db.Column(Integer, primary_key=True)
    email = db.Column(String, unique=True, nullable=False)
    password = db.Column(String, nullable=False)
    name = db.Column(String)