# Objective
Runs a flask app that connects to git to list the public gists
https://docs.github.com/en/rest/gists/gists?apiVersion=2022-11-28#list-public-gists

# Supported endpoints (Supports only 'GET' methods)
1. "/" - Loads a default response
2. "/helloworld" - Loads a hello world response
3. "/<user>" - Loads the public gists of the user provided in the param
    1. Paginated response is supported

# To run locally
> pip3 install requirements.txt(Inside a virtual env)
> python3 route.py (Starts the flask api server)
> python3 api_test.py (Tests the api endpoints exposed by flask. Internally connects to localhost.)

# Pytest 
> python3 -m pytest 
Above command runs the unit test cases written against the code

# Docker image setup
To build the image:
> docker build -t <registry_name>/<image_name>:v1.0.0 .
> docker run --name flaskapp -p 8080:8080 <registry_name>/<image_name>:v1.0.0

Once the docker container is running, you can optionally use the browser to load the localhost:8080 to see the respective gists for the user

