from flask_restful import Api
from flask import Blueprint
from .task import TaskById, ListAllTasks, AddTask

api_blueprint = Blueprint('api', __name__)
api = Api()
api.init_app(api_blueprint)

#task route
api.add_resource(ListAllTasks, '/task')
api.add_resource(AddTask, '/task')
api.add_resource(TaskById, '/task/<int:id>')