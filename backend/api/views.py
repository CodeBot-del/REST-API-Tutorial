from django.http import JsonResponse
import json

from products.models import Product


def api_home(request, *args, **kwargs):
    # print(request.GET) #get the url query params
    # print(request.POST) #get the url post params
    # body = request.body #byte string of JSON data
    # data = {}
    # try:
    #     data = json.loads(body) #string of json data -> Python Dictionary
    # except:
    #     pass
    # print(data)
    # # data['headers'] = request.headers #passing headers without converting them to dict will cause serialization error
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers) #convert headers to dict
    # data['content_type'] = request.content_type
    
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        #this is not right
        #we need to do serialization
        # i.e we take model instance (model_data)
        # turn to a Python Dictionary
        # return JSON to my client
    return JsonResponse(data)
