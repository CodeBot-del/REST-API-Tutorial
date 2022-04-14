import requests 

endpoint = "http://localhost:8000/api/products/10/"    #"http://127.0.0.1:8000/"

get_response = requests.get(endpoint) 
print(get_response.json()) 

title_ret = get_response.json()['title']
print("The retrieved title is "+title_ret)