from django.urls import path, include
from django.contrib import admin
from .views import register_user
from django.conf import settings
from django.conf.urls.static import static
from views import product_list

urlpatterns = [
    path('api/register/', register_user),
    path('api/products/', product_list),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
