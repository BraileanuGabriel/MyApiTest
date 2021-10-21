from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import ProductsView, ImageViewSet

urlpatterns = format_suffix_patterns( [
    path('', views.api_root),
    path('products/', views.ProductsView.as_view(), name='products-list'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='producte-detail'),
    path('image_upload/', ImageViewSet.as_view(), name='images_upload'),
])