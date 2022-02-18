from flask import Flask
from app.config.config import Config
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)


# main routes
from app import routes


# Blueprint routes
from app.traccar.routes import traccar
from app.config.routes import config

app.register_blueprint(traccar)
app.register_blueprint(config)


