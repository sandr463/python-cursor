from flask import Flask
from flask import request

import json

app = Flask(__name__)

MEMBERS = {
    'denis': {'age': 25, 'gender': 'male', 'name': 'Denis'},
    'olga': {'age': 35, 'gender': 'female', 'name': 'Olga'}
}


def add_member(name, age, gender):
    MEMBERS[name] = {"age": age, "name": name, "gender": gender}
    responce_data = {"jsonrpc": "2.0", "result": f"We add your member {MEMBERS[name]}"}
    return json.dumps(responce_data)


def get_member(name):
    responce_data = {"jsonrpc": "2.0", "result": MEMBERS[name.lower()]}
    return json.dumps(responce_data)


METHODS = {
    "getMember": get_member,
    "addMember": add_member
}


@app.route('/', methods=['POST'])
def handle():
    data = json.loads(request.data.decode('utf-8'))
    method_view = METHODS.get(data.get('method'))
    if not method_view:
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = method_view(**data.get("params"))
    return result


@app.route('/ping', methods=['POST'])
def ping():
    data = json.loads(request.data.decode('utf-8'))
    print(data.get('method'))
    if data.get('method') != 'ping':
        return json.dumps({"error": {"code": -32601, "message": "Method not found"}})

    result = {"jsonrpc": "2.0", "result": "Hello my Sir!"}
    return json.dumps(result)


if __name__ == '__main__':
    with open('settings.json') as ff:
        settings = json.load(ff)

    app.run(host=settings["HOST"], port=settings["PORT"], debug=settings["debug_mode"])
