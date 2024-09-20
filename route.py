from flask import Flask, jsonify
from flask_restful import Api, Resource, abort
import requests

## Creates new flask application
app = Flask(__name__)
## Wraps app in API indicating we are using RESTful API
api = Api(app)  

GITHUB_BASE_URL = "https://api.github.com/users/"

#The class is inheriting Resource module and we are going to override the methods on it
class Default(Resource):
    def get(self):
        #The data that we return should be serializable
        return {"data" : "Use /helloworld or /user params"}

class HelloWorld(Resource):
    def get(self):
        return {"data" : "Hello World!"}
    
class GitHubUserGist(Resource):
    def get(self, user):
        response = requests.get(GITHUB_BASE_URL + user + "/gists?per_page=100&page=1")
        gists = response.json()
        # Code responsible for looping through pages to get the final response
        while 'next' in response.links.keys():
            response = requests.get(GITHUB_BASE_URL + user + "/gists") 
            gists.extend(response.json())
        if gists:
            return response.json(), 200
        else:
            #Responds with a custom message if there are no public gists present
            abort(404, message="There are no public gists for this user. Please check")

#Register this as a resource of the api
#<string:name>  - user to type some string after hello world and this will be added to the variable name
api.add_resource(Default, "/")
api.add_resource(HelloWorld, "/helloworld")
api.add_resource(GitHubUserGist, "/<string:user>")



## Calls the flask app
if __name__ == "__main__":
    ## Enabling debug mode - Remove debug in prod envs
    app.run(debug=True, host='0.0.0.0', port=8080)