from django.db import models


class Producte(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    add_at = models.DateTimeField(auto_now_add=True)
    sku = models.CharField(max_length=8)
    objects = models.Manager()

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Producte, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/')


