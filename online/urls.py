from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('products.urls', namespace='mainapp')),
    path('admin/', admin.site.urls),
]
