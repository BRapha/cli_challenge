from tabs_service import app, mongo
from flask import request, jsonify


@app.route('/')
def home():
    return "Use /tabs route to access tabs."


@app.route('/tabs', methods=['GET'])
@app.route('/tabs/', methods=['GET'])
def get_all_tabs():
    return jsonify([tab for tab in mongo.db.tabs.find()])


@app.route('/tabs', methods=['POST'])
def save_tab():
    tab_json = request.get_json()
    if not tab_json:
        return "Please provide a JSON object in the request body!", 204

    tab_id = mongo.db.tabs.insert(tab_json)
    return jsonify({"_id": tab_id}), 201


@app.route('/tabs/<object_id:tab_id>', methods=['GET'])
def get_tab(tab_id):
    tab = mongo.db.tabs.find_one({'_id': tab_id})
    return (jsonify(tab), 200) if tab else ("", 204)


@app.route('/tabs/<object_id:tab_id>', methods=['PUT'])
def update_tab(tab_id):
    """"Only updates existing elements. Does not insert a new document if tab_id not present."""
    tab_json = request.get_json()
    result = mongo.db.tabs.replace_one({'_id': tab_id}, tab_json, upsert=False)    # set upsert=True to insert new doc
    return (jsonify({"_id": tab_id}), 200) if result.modified_count > 0 else ("", 204)


@app.route('/tabs/<object_id:tab_id>', methods=['DELETE'])
def delete_tab(tab_id):
    mongo.db.tabs.delete_one({'_id': tab_id})
    return "", 204
