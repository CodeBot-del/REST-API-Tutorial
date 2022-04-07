import requests 

# endpoint = "https://httpbin.org/status/200"
endpoint = "https://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query": "Hello World"}) #emulate an HTTP Request
print(get_response.json()) #print raw text response

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
#  JSON ==> JavaScript Object Notation ~ Python Dictionary

print(get_response.status_code)