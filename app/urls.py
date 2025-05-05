from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import register_user, product_list

urlpatterns = [
    path('api/register/', register_user),
    path('api/products/', product_list),  # Bu joy to'g'ri ekanligini tekshiring
    path('admin/', admin.site.urls),
]