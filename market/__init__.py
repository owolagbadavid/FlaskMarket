from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SECRET_KEY'] = '87ddc7dc2ca2f007ee13dca6'
db = SQLAlchemy(app)

__import__('market.routes')
