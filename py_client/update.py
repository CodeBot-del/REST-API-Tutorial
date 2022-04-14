import requests 

endpoint = "http://localhost:8000/api/products/2/update/"    #"http://127.0.0.1:8000/"

data ={
    "title": "Am just getting updated, yikes",
    "price": 349.85
}


get_response = requests.put(endpoint, json=data) 
print(get_response.json()) 
