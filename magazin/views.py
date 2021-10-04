from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Producte
from .serializers import ProductsSerializer, ProductSerializer, ProductAddSerializer
from rest_framework import generics
from rest_framework import renderers


class ProductHighlight(generics.GenericAPIView):
    queryset = Producte.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self):
        product = self.get_object()
        return Response(product.highlighted)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Products': reverse('products-list', request=request, format=format),
    })


class ProductsView(generics.ListCreateAPIView):
    queryset = Producte.objects.all()
    serializer_class = ProductsSerializer



class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producte.objects.all()
    serializer_class = ProductSerializer
