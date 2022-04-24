from flask import jsonify
from flask_restful import reqparse, abort, Resource
from app.models.Task import Task

TASKS = {}

## handling if id not exist
def abort_if_task_doesnt_exist(id):
    if id not in TASKS:
        abort(404, message="Task {} doesn't exist".format(id))

## generate new id
def new_id():
  if len(TASKS.keys()) == 0:
    return 0
  else:
    return max(TASKS.keys()) + 1

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('status')

class TaskById(Resource):
    def get(self, id):
        abort_if_task_doesnt_exist(int(id))
        return TASKS[int(id)].jsonify()

    def put(self, id):
        abort_if_task_doesnt_exist(int(id))
        args = parser.parse_args()
        task = Task(int(id), args['name'], args['status'])
        TASKS[task.id] = task
        return task.jsonify()
    
    def delete(self, id):
        abort_if_task_doesnt_exist(int(id))
        del TASKS[int(id)]
        return ''

class ListAllTasks(Resource):
    def get(self):
        return jsonify(list(map(lambda i: i.toJSON(), TASKS.values())))

class AddTask(Resource):
    def post(self):
        args = parser.parse_args()
        task = Task(new_id(), args['name'], 0)
        TASKS[task.id] = task
        response = task.jsonify()
        response.status_code = 201
        return response