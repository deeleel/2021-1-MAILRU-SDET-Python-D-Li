from flask import Flask, jsonify
from default_user import DEFAULT_USER
import settings
import os

app = Flask(__name__)

DATA = {DEFAULT_USER['name']: 1}


@app.route('/vk_id/<name>', methods=['GET'])
def get_user_id(name):

    id = DATA.get(name)
    print(id)
    if id is not None:
        return jsonify({'vk_id': id}), '200 OK'
    else:
        return jsonify({}), '404 Not Found'


@app.route('/add_user/<name>', methods=['POST'])
def add_user(name):
    if name not in DATA:
        id = DATA.get(list(DATA)[-1]) + 1
        DATA.update({name: id})
        return jsonify({'name': name,'vk_id': id}), '201 CREATED'
    else:
        return jsonify({}), '304 Not Changed'



if __name__ == '__main__':
    host = os.environ.get('MOCK_HOST', settings.MOCK_HOST)
    port = os.environ.get('MOCK_PORT', settings.MOCK_PORT)

    app.run(host, port)
