import json
from flask import jsonify

class Task:
  def __init__(self, id, name, status):
    self.id = id
    self.name = name
    self.status = status
  
  def toJSON(self):
      return { "id": self.id, "name": self.name, "status": self.status}

  def jsonify(self):
      
      return jsonify(self.toJSON())