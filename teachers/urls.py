from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome),
    path('about', views.about),
    path('services', views.services),
    path('contact', views.contact)
]