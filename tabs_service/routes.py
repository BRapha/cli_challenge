from tabs_service import app
from flask import request, jsonify

@app.route('/')
def home():
    return "Hello World"


@app.route('/tabs', methods=['GET', 'POST'])
def tabs():
    if request.method == 'GET':
        print("GET tabs")
    elif request.method == 'POST':
        content = request.get_json()
        print(content)
        print("POST tabs")
    return 'Done'


@app.route('/tabs/<int:tabs_id>', methods=['PUT', 'DELETE'])
def change_tabs(tabs_id):
    if request.method == 'DELETE':
        print(f"DELETE tabs with id: {tabs_id}")
    elif request.method == 'PUT':
        print(f"UPDATE tabs with id: {tabs_id}")

    return 'Done'