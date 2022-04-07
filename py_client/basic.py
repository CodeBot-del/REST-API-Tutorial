import requests 

# endpoint = "https://httpbin.org/status/200"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"    #"http://127.0.0.1:8000/"

get_response = requests.get(endpoint,params={"product_id": 123}) #emulate an HTTP Request
print(get_response.json()) 
# print(get_response.status_code)
# print(get_response.text) #print raw text response


# HTTP Request -> HTML
# REST API HTTP Request -> JSON
#  JSON ==> JavaScript Object Notation ~ Python Dictionary

