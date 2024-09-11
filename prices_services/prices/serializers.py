from rest_framework import serializers
from .models import Price

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ['brand_id', 'start_date', 'end_date', 'price_list', 'product_id', 'priority', 'price', 'curr']
