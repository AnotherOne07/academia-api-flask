import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

# load_dotenv()

app = Flask(__name__)
# db_url = os.environ.get("DATABASE_URL")
# conn = psycopg2.connect(db_url)

from views import *
