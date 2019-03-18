from flask import Flask
from flask_pymongo import PyMongo
from .mongo_util import MongoJSONEncoder, ObjectIdConverter


app = Flask(__name__)
db_name = "tabDB"
app.config["MONGO_DBNAME"] = db_name    # set default mongo db instance
app.config["MONGO_URI"] = "mongodb://localhost:27017/" + db_name
app.json_encoder = MongoJSONEncoder    # Set custom encoder to handle MongoDB-specific data types, e.g. ObjectID
app.url_map.converters['object_id'] = ObjectIdConverter    # handle auto type conversion of URL parameters
mongo = PyMongo(app)


from tabs_service import routes