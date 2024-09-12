import pytest
from django.urls import reverse
from rest_framework.test import APIClient
import pytz
from datetime import datetime
from prices.models import Price

@pytest.mark.django_db
class TestPriceAPI:

    def setup_method(self):
        self.client = APIClient()
        # Insertar datos en la base de datos directamente si no existen
        if not Price.objects.filter(product_id=35455, brand_id=1).exists():
            Price.objects.create(
                product_id=35455,
                brand_id=1,
                price_list=1,
                start_date="2020-06-14T00:00:00Z",
                end_date="2020-12-31T23:59:59Z",
                price=35.50,
                priority=0,
                curr="USD"  # Especificar la moneda
            )
            Price.objects.create(
                product_id=35455,
                brand_id=1,
                price_list=2,
                start_date="2020-06-14T15:00:00Z",
                end_date="2020-06-14T18:30:00Z",
                price=25.45,
                priority=1,
                curr="USD"  # Especificar la moneda
            )
            Price.objects.create(
                product_id=35455,
                brand_id=1,
                price_list=3,
                start_date="2020-06-15T00:00:00Z",
                end_date="2020-06-15T11:00:00Z",
                price=30.50,
                priority=1,
                curr="USD"  # Especificar la moneda
            )
            Price.objects.create(
                product_id=35455,
                brand_id=1,
                price_list=4,
                start_date="2020-06-15T16:00:00Z",
                end_date="2020-12-31T23:59:59Z",
                price=38.95,
                priority=1,
                curr="USD"  # Especificar la moneda
            )

    def normalize_response(self, response):
        """Convierte las fechas a cadenas ISO y el precio a float para la comparación."""
        response.data['start_date'] = response.data['start_date'].isoformat()
        response.data['end_date'] = response.data['end_date'].isoformat()
        response.data['price'] = float(response.data['price'])  # Asegura que el precio esté en formato float
        return response.data

    # Test 1: petición a las 10:00 del día 14 del producto 35455 para la brand 1 (STORE_X)
    def test_price_at_10_am_14th_june(self):
        application_date = datetime(2020, 6, 14, 10, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 1,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 1,
            "price_list": 1,
            "start_date": "2020-06-14T00:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 35.50
        }

    # Test 2: petición a las 16:00 del día 14 del producto 35455 para la brand 1 (STORE_X)
    def test_price_at_16_pm_14th_june(self):
        application_date = datetime(2020, 6, 14, 16, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 1,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 1,
            "price_list": 2,
            "start_date": "2020-06-14T15:00:00+00:00",
            "end_date": "2020-06-14T18:30:00+00:00",
            "price": 25.45
        }

    # Test 3: petición a las 21:00 del día 14 del producto 35455 para la brand 1 (STORE_X)
    def test_price_at_21_pm_14th_june(self):
        application_date = datetime(2020, 6, 14, 21, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 1,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 1,
            "price_list": 1,
            "start_date": "2020-06-14T00:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 35.50
        }

    # Test 4: petición a las 10:00 del día 15 del producto 35455 para la brand 1 (STORE_X)
    def test_price_at_10_am_15th_june(self):
        application_date = datetime(2020, 6, 15, 10, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 1,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 1,
            "price_list": 3,
            "start_date": "2020-06-15T00:00:00+00:00",
            "end_date": "2020-06-15T11:00:00+00:00",
            "price": 30.50
        }

    # Test 5: petición a las 21:00 del día 16 del producto 35455 para la brand 1 (STORE_X)
    def test_price_at_21_pm_16th_june(self):
        application_date = datetime(2020, 6, 16, 21, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 1,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 1,
            "price_list": 4,
            "start_date": "2020-06-15T16:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 38.95
        }
