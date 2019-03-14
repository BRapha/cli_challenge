from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'service_db'
app.config["MONGO_URI"] = "mongodb://localhost:27017/service_db"
mongo = PyMongo(app)

from tabs_service import routes