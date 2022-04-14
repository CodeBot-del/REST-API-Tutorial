import requests 

endpoint = "http://localhost:8000/api/products/"    #"http://127.0.0.1:8000/"

data={
    "title": "Iphone 13 Pro",
    "price": 32.99
}

get_response = requests.post(endpoint, json=data) 
print(get_response.json()) 

title_ret = get_response.json()['title']
print("The retrieved title is "+title_ret)