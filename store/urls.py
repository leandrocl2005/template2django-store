from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import (home, product_detail, products_list)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('products/', products_list),
    path('product/<int:pk>/', product_detail),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
