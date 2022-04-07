from django.http import JsonResponse, HttpResponse
import json
from django.forms.models import model_to_dict

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
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
