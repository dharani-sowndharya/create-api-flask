import requests

BASE = "http://127.0.0.1:8080/"

#Should print the default message
response = requests.get(BASE)
print(response.json())

print('─' * 50)
#Should print the Hello world message
response = requests.get(BASE + "helloworld")
print(response.json())

print('─' * 50)
#Should print the actual gists
response = requests.get(BASE + "octocat")
print(response.json())

print('─' * 50)
#Should print the message to say that there are no public gists for the user
response = requests.get(BASE + "blah")
print(response.json())