from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.http import Http404
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializer

# product create API view 
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    # in case you wanna assign something when the product is created
    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        # print(serializer.validated_data)  #serializer.validated_data returns the data thats coming from the user request
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        
        
        serializer.save(content=content)
        # You can also send a Django signal

product_list_create_view = ProductListCreateAPIView.as_view()

# product retrieve API View
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
product_detail_view = ProductDetailAPIView.as_view()


# product list API View 
class ProductListAPIView(generics.ListAPIView):
    
    """
    Not gonna use this method
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
product_list_view = ProductListAPIView.as_view()


# Function based views for create, retrieve or list.. (all of the operations in one function)
@api_view(['GET', 'POST'])
def product_alt_view(request, *args, **kwargs):
    method = request.method
    
    # check for the type of request method to specify actions
    if method == "GET":
        pass
        # url_args??
        #get request as in detail view
        #list view
    
    if method == "POST":
        # create item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):  #checks if the data sent to this view endpoint via API matches how the serializer data is formatted in serializers.py
            # instance = serializer.save()
            #instance = form.save()
            print(serializer.data)
            return Response(serializer.data)
        return Response({"Invalid": "not good data"}, 
        status=400)
