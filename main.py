from flask import Flask, request
import flask

from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

# Create a mini database to return details from 
names = {
            "mike": {"age":21, "gender":"male"},
            "vicky": {"age":21, "gender":"female"}
        }

# Create our resource and appropriate REST methods
class HelloWorld(Resource):
    def get(self, name):
        return names[name]
    def post(self):
        return {"data":"Posted Hello World"}


dogPutArgs = reqparse.RequestParser()
dogPutArgs.add_argument("name", type=str, help="Name of the dog is required", required = True)
dogPutArgs.add_argument("age", type=int, help = "Age of the dog is required", required = True)
dogPutArgs.add_argument("breed", type=str, help = "What breed of dog is required", required = True)

# In memory dogs database
dogs = {}

def abortIfDogExists (dogId):
    if dogId in dogs:
        abort(409, message="Dog already exists with Id " + str(dogId))

def abortIfDogDoesNotExist(dogId):
    if dogId not in dogs:
        abort(404, message="Dog Id " + str(dogId) + " is not valid")
        
class Dog(Resource):
    def get(self, dogId):
        abortIfDogDoesNotExist(dogId)
        return dogs[dogId]
    
    def put (self, dogId):
        abortIfDogExists(dogId)
        args = dogPutArgs.parse_args()
        dogs[dogId] = args
        
        return dogs[dogId], 201
    
    def delete (self, dogId):
        abortIfDogDoesNotExist (dogId)
        del dogs[dogId]
        return '', 204

# Add endpoint
api.add_resource (HelloWorld, "/helloworld/<string:name>")
api.add_resource (Dog, "/dogs/<int:dogId>")

if __name__ =="__main__":
    app.run (debug=True)

