from tabs_service import app, mongo
from flask import request, jsonify
from bson.json_util import loads, dumps


@app.route('/')
def home():
    return "Use /tabs route to access tabs."


@app.route('/tabs', methods=['GET'])
def get_all_tabs():
    # returns JSON array of all tabs in DB
    out = []
    for tab in mongo.db.tabs.find():
        out.append(tab)

    return jsonify(out)


@app.route('/tabs', methods=['POST'])
def save_tab():
    content = request.get_json()
    print(f"response = {content}")
    if not content:
        return "Please provide a JSON object in the request body!"

    tab_collection = mongo.db.tabs
    tab_id = tab_collection.insert(content)
    return "New tabs inserted"


@app.route('/tabs/<int:tab_id>', methods=['PUT'])
def override_tab(tab_id):
    #TODO: Override tab from MongoDB
    return f"Did override {tabs_id}"



@app.route('/tabs/<int:tab_id>', methods=['DELETE'])
def delete_tab(tab_id):
    #TODO: Delete tab from MongoDB
    return f"Deleted {tab_id}"