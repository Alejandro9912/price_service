from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prices.urls')),  # Aquí estás enlazando el archivo urls.py de 'prices'
]
