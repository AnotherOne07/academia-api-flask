from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

# db.init_app(app)

# from models import db
from views import app_routes

app.register_blueprint(app_routes)


# db_url = os.environ.get("DATABASE_URL")
# conn = psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="postgres",
#     host=db_url,
#     port=5432)

if __name__ == '__main__':
    app.run(debug=True)
