from flask import Flask
import json
from flask import render_template
from flask import request







app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/v1')
def apiv1():
    return render_template('apiv1docs.html')


@app.route('/api/v1/uploadentry/', methods=['POST'])
def uploadentry():
    with open('entrys.json', 'r') as f:
        json_data = json.load(f)
    content = request.json
    data = content['data']
    entryname = content['entryname']
    if entryname in json_data:
        return 'Please Select another entry name as this one is already in use.'
    else:
        json_data[entryname] = data
        with open('entrys.json', 'w+') as f:
            json.dump(json_data, f, indent=4)
        return f'Added Entry {entryname} to the database.', 200


@app.route('/api/v1/entry/<entryname>', methods=['GET'])
def getentry(entryname):
    with open('entrys.json', 'r') as f:
        json_data = json.load(f)
    if entryname not in json_data:
        return 'Entry With The name ' + entryname + ' doesnt exist.', 404
    else:
        return json_data[entryname], 200

