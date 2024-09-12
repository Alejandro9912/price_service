from django.urls import path
from .views_api import PriceView

urlpatterns = [
    path('price/', PriceView.as_view(), name='price-view'),  # endpoint API
]
