from flask import Flask

app = Flask(__name__)

from tabs_service import routes