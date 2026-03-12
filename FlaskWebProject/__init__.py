"""
The flask application package.
"""
import logging
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session

app = Flask(__name__)
app.config.from_object(Config)

# Logging configuration
logging.basicConfig(level=logging.INFO)
app.logger.setLevel(logging.INFO)
app.logger.info("Application startup")

Session(app)

db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

# Import models and views
import FlaskWebProject.models
import FlaskWebProject.views

# Create database tables automatically
with app.app_context():
    db.create_all()
