#from flask import flask
import flask

from flask_restful import Api, Resource

app = flask.Flask(__name__)
api = Api(app)

# Create our resource and appropriate REST methods
class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello World"}
    def post(self):
        return {"data":"Psoted Hello World"}

# Add endpoint
api.add_resource (HelloWorld, "/helloworld")

if __name__ =="__main__":
    app.run (debug=True)

