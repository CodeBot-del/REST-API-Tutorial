from rest_framework import generics

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

