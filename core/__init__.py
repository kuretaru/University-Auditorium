import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Configuration
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from .auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from .audithory import audithory as audithory_blueprint
app.register_blueprint(audithory_blueprint)

from core import views, models
