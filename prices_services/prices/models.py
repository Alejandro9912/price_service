from django.db import models

class Price(models.Model):
    brand_id = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price_list = models.IntegerField()
    product_id = models.IntegerField()
    priority = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    curr = models.CharField(max_length=10)
