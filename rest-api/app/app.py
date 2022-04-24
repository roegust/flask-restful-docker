from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from .apis import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix='')


def create_app():
    return app