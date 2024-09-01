from flask import Flask, request
#import flask

from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
SQLFILENAME = "sqlite:///database.db" 
app.config["SQLALCHEMY_DATABASE_URI"] = SQLFILENAME
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class DogModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer, nullable = False)
    breed = db.Column(db.String(100), nullable = False)

    # String representation of the object
    def __repr__(self):
        return f"Dog(name = {self.name}, age={self.age}, breed={self.breed})"

# Creates database using the object
# MUST ONLY RUN THIS ONCE SO WILL CHECK IF FILE EXISTS FIRST
from pathlib import Path

file = Path(SQLFILENAME)

if file.exists():
    pass
else:
    db.create_all()

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

dogUpdateArgs = reqparse.RequestParser()
dogUpdateArgs.add_argument("name", type=str, help="Name of the dog is required")
dogUpdateArgs.add_argument("age", type=int, help = "Age of the dog is required")
dogUpdateArgs.add_argument("breed", type=str, help = "What breed of dog is required")

""" def abortIfDogExists (dogId):
    if dogId in dogs:
        abort(409, message="Dog already exists with Id " + str(dogId))

def abortIfDogDoesNotExist(dogId):
    if dogId not in dogs:
        abort(404, message="Dog Id " + str(dogId) + " is not valid")
 """        

resourceFields = {
    "id": fields.Integer,
    "name": fields.String,
    "age": fields.Integer,
    "breed": fields.String
}
class Dog(Resource):
    @marshal_with(resourceFields)
    def get(self, dogId):
        result = DogModel.query.filter_by(id = dogId).first()

        if not result:
            abort(404, message="Could not find Dog")

        return result
    
    def put (self, dogId):
        args = dogPutArgs.parse_args()
        result = DogModel.query.filter_by(id = dogId).first()
        if result:
            abort(409, message="Dog ID already taken")
                  
        dog = DogModel (id = dogId, name = args["name"], age = args["age"], breed = args["breed"])

        try:
            db.session.add (dog)
            db.session.commit()
        
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")

        return dog, 201
    
    def patch(self, dogId):
        args = dogUpdateArgs.parse_args()
        result = DogModel.query.filter_by(id = dogId).first()
        if not result:
            abort(409, message="Dog not found - cannot update")

        if args["name"]:
            result.name = args["name"]
        if args["age"]:
            result.age = args["age"]
        if args["breed"]:
            result.breed = args["breed"]
        
        try:
            #db.session.add(result)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred: {e}")

        return result, 201

    # TO DO
    def update (self, dogId):
        args = dogPutArgs.parse_args()
        
        return
    
    # TO DO
    def delete (self, dogId):
        result = DogModel.query.filter_by(id = dogId).first()
        if not result:
            abort(409, message="Dog not found - cannot delete")

        try:
            db.session.delete(result)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred trying to delete dog {dogId}: {e}")         
        
        return 201

# Add endpoint
api.add_resource (HelloWorld, "/helloworld/<string:name>")
api.add_resource (Dog, "/dogs/<int:dogId>")

if __name__ =="__main__":
    app.run (debug=True)

