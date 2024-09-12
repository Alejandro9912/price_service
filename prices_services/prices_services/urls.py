from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prices.urls')),  # Enlace al archivo urls.py de la aplicación 'prices'
]
