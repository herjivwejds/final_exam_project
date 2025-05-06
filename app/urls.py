from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import register_user, product_list
from . import views

urlpatterns = [
    path('register/', register_user),
    path('products/', product_list),
]
