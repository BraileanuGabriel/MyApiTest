from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = format_suffix_patterns( [
    path('', views.api_root),
    path('products/', views.ProductsView.as_view(), name='products-list'),
    path('add/', views.ProductsAdd.as_view(), name='add'),
    path('products/<int:pk>/', views.ProductView.as_view(), name='producte-detail'),
    path('snippets/<int:pk>/highlight/', views.ProductHighlight.as_view(), name='products-highlight'),
])