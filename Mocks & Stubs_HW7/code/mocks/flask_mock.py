import threading
import json

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if SURNAME_DATA.get(name):
        surname = SURNAME_DATA.get(name)
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404

@app.route('/update_surname/<name>', methods=['PUT'])
def update_user_surname(name):
    surname2 = json.loads(request.data)['new_surname']
    if SURNAME_DATA.get(name):
        SURNAME_DATA[name] = surname2
        return jsonify(surname2), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404

@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if SURNAME_DATA.get(name):
        SURNAME_DATA.pop(name)
        return jsonify(f'Surname for user {name} deleted'), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
