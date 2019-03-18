from flask.json import JSONEncoder
from bson import ObjectId
from werkzeug.routing import BaseConverter


# With inspiration from https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable
class MongoJSONEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)

        return super().default(o)


class ObjectIdConverter(BaseConverter):
    def to_python(self, value):
        return ObjectId(value)

    def to_url(self, value):
        return str(value)
