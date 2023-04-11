from flask import Flask
from logging.config import dictConfig
from .config import AppConfig
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
    }},
})

app.config.from_object(AppConfig)

db.init_app(app)

from .views import *
from .models import *

with app.app_context():
    db.create_all()