from rest_framework import serializers

from .models import Producte, ProductImage


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Producte
        fields = ['url', 'name', 'price', 'image', 'description', 'sku']
        extra_kwargs = {
            'description': {'write_only': True},
            'sku': {'write_only': True}
        }

    def get_image(self, obj):
        image = obj.productimage_set.first()
        if image:
            request = self.context.get("request")
            return request.build_absolute_uri(image.image.url)
        else:
            return None


class ProductSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()

    class Meta:
        model = Producte
        fields = "__all__"

    def get_images(self, obj):
        urls_list = []
        images = obj.productimage_set.all()
        request = self.context.get("request")
        for image in images:
            urls_list.append(request.build_absolute_uri(image.image.url))

        return urls_list

