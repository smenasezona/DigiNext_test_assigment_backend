import sqlite3

from flask import Flask, request, jsonify, g
from flask_cors import CORS

from entities import *

app = Flask(__name__)
CORS(app)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('./identifier.sqlites')
    return db


@app.before_request
def before_request():
    g.db = get_db()


@app.teardown_request
def teardown_request(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/entities', methods=['POST'])
def create_entity_route():
    data = request.get_json()
    create_entity(data['name'], data['coordinate'], data['labels'])
    return jsonify({'message': 'Entity created successfully'}), 201


@app.route('/entities/<name>', methods=['GET'])
def get_entity_route(name):
    entity = get_entity(name)
    if entity is not None:
        return jsonify({'name': entity.name, 'coordinate': entity.coordinate, 'labels': entity.labels}), 200
    else:
        return jsonify({'message': 'Entity not found'}), 404


@app.route('/entities/<name>', methods=['PUT'])
def update_entity_route(name):
    data = request.get_json()
    update_entity(name, data['coordinate'], data['labels'])
    return jsonify({'message': 'Entity updated successfully'}), 200


@app.route('/entities/<name>', methods=['DELETE'])
def delete_entity_route(name):
    delete_entity(name)
    return jsonify({'message': 'Entity deleted successfully'}), 200


@app.route('/entities', methods=['GET'])
def get_all_entities_route():
    entities = get_all_entities()
    return jsonify(
        [{'name': entity.name, 'coordinate': entity.coordinate, 'labels': entity.labels} for entity in entities]), 200


@app.route('/entities/filter/<label>', methods=['GET'])
def filter_entities_route(label):
    entities = filter_entities(label)
    return jsonify(
        [{'name': entity.name, 'coordinate': entity.coordinate, 'labels': entity.labels} for entity in entities]), 200


@app.route('/coordinates', methods=['GET'])
def get_coordinates_route():
    coordinates = get_coordinates()
    return jsonify({'coordinates': coordinates})


if __name__ == '__main__':
    app.run(debug=True)
