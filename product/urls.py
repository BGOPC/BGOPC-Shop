from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_red),
    path('home', views.home, name="home"),
    path('products', views.products, name="products"),
    path('product/<slug:ps>', views.product, name="product-det/"),
]
