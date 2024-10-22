from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from views import app_routes

app.register_blueprint(app_routes)

if __name__ == '__main__':
    app.run(debug=True)
