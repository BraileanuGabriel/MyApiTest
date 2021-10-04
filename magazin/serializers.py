from rest_framework import serializers
from .models import Producte


class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producte
        fields = '__all__'
        # write_only_fields = ['description', 'add_at', 'photo2', 'photo3', 'sku']
        extra_kwargs = {
            'description': {'write_only': True},
            # 'add_at': {'write_only': True},
            'photo2': {'write_only': True},
            'photo3': {'write_only': True},
            'sku': {'write_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['name', 'price', 'description', 'add_at', 'photo1', 'photo2', 'photo3', 'sku']
        read_only_fields = ['add_at', 'photo1', 'photo2', 'photo3']


class ProductAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producte
        fields = ['name', 'price', 'description', 'add_at', 'photo1', 'photo2', 'photo3', 'sku']
