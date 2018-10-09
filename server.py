from tasks import tasks as get_tasks_list
from tasks import create as create_task_list
from tasks import update as update_task_list
from tasks import delete as delete_task_list
from tasks import get as get_task_list

from users import get_user

from flask import Flask
from flask import jsonify
from flask import abort
from flask import request
from flask import make_response
from flask import url_for

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['url'] = url_for('get_task', task_id=task['id'], _external=True) #Absotule url
        else:
            new_task[field] = task[field]
    return new_task

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)

@auth.get_password
def get_password(username):
    return get_user(username)
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'task not found'}),  400)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    order = request.args.get('order', False)
    tasks = get_tasks_list()

    if order:
        print("Entramos aquí")
        tasks = sorted(tasks, key= lambda k : k['priority'], reverse=True)

    return jsonify( {'tasks' : [make_public_task(task) for task in tasks]} ) #return jsonify( {'tasks' : get_tasks_list() } )

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = get_task_list(task_id)
    if task == None:
        abort(404)
    return jsonify({'task' : task})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)

    title = request.json.get('title', '')
    description = request.json.get('description', '')

    return jsonify({'task': create_task_list(title, description)})

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):

    title = request.json.get('title', '')
    description = request.json.get('description', '')
    done = request.json.get('done', False)

    task = update_task_list(task_id, title, description, done)
    if task:
        return jsonify({'task' : task})
    return abort(400)

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if not delete_task_list(task_id):
        abort(404)
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
