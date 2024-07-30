from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
# wrapping app in an api - initialising a restful api
api = Api(app)

# Example: creating a resource
class HelloWorld(Resource):
    def get(self):
        return {"data":"Hello World"}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == "__main__":
    app.run(debug=True)