from route import app

def test_route_default():
    response = app.test_client().get('/')
    assert response.status_code == 200
    assert b'{"data": "Use /helloworld or /user params"}\n'in response.data 

def test_route_hello_world():
    response = app.test_client().get('/helloworld')
    assert response.status_code == 200
    assert b'{"data": "Hello World!"}\n'in response.data 

def test_route():
    response = app.test_client().get('/octocat')
    assert response.status_code == 200
    
def test_route_404():
    response = app.test_client().get('/nill')
    assert response.status_code == 404
    assert b'{"message": "There are no public gists for this user. Please check"}\n' in response.data