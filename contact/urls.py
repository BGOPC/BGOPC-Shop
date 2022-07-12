from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('response/<int:cid>', views.response, name='response'),
    path('about', views.about, name='about'),
]
