from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_red),
    path('products', views.products, name="products"),
    path('product/<int:pid>', views.product, name="product"),
]