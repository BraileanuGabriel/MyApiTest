from rest_framework import serializers
from .models import Producte


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producte
        fields = ['url', 'name', 'price', 'photo1']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['name', 'price', 'description', 'add_at', 'photo1', 'photo2', 'photo3', 'sku']
        read_only_fields = ['add_at', 'photo1', 'photo2', 'photo3']

class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['name', 'price', 'description', 'add_at', 'photo1', 'photo2', 'photo3', 'sku']
