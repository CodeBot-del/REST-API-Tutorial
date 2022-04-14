import json
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from products.serializers import ProductSerializer


@api_view(['POST'])#pass the http methods you want to allow
def api_home(request, *args, **kwargs):
    """
    DRF API VIEW
    """
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  #checks if the data sent to this view endpoint via API matches how the serializer data is formatted in serializers.py
        # instance = serializer.save()
        #instance = form.save()
        print(serializer.data)
        return Response(serializer.data)
    return Response({"Invalid": "not good data"}, 
    status=400)
