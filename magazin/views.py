from django.db import router
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Producte, ProductImage
from .serializers import ProductsSerializer, ProductSerializer, ImageSerializer
from rest_framework import generics, viewsets, filters
from rest_framework import renderers



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Products': reverse('products-list', request=request, format=format),
        'Images': reverse('images_upload', request=request, format=format),
    })

class ImageViewSet(generics.CreateAPIView):
    queryset = ProductImage.objects.all()
    serializer_class = ImageSerializer



class ProductsView(generics.ListCreateAPIView):
    serializer_class = ProductsSerializer
    queryset = Producte.objects.all()



class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producte.objects.all()
    serializer_class = ProductSerializer
