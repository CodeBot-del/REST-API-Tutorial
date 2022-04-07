from django.http import JsonResponse
import json


def api_home(request, *args, **kwargs):
    body = request.body #byte string of JSON data
    data = {}
    try:
        data = json.loads(body) #string of json data -> Python Dictionary
    except:
        pass
    print(data)
    # data['headers'] = request.headers
    data['content_type'] = request.content_type
    return JsonResponse(data)
