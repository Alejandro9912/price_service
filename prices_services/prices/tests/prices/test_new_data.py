import pytest
from django.urls import reverse
from rest_framework.test import APIClient
import pytz
from datetime import datetime
from prices.models import Price

@pytest.fixture
def create_new_prices(db):
    # Grupo 1: product_id 35455, brand_id 2
    Price.objects.create(
        product_id=35455,
        brand_id=2,
        price_list=1,
        start_date="2020-06-14T00:00:00Z",
        end_date="2020-12-31T23:59:59Z",
        price=36.50,
        priority=0
    )
    Price.objects.create(
        product_id=35455,
        brand_id=2,
        price_list=2,
        start_date="2020-06-14T15:00:00Z",
        end_date="2020-06-14T18:30:00Z",
        price=26.45,
        priority=1
    )
    Price.objects.create(
        product_id=35455,
        brand_id=2,
        price_list=3,
        start_date="2020-06-15T00:00:00Z",
        end_date="2020-06-15T11:00:00Z",
        price=31.50,
        priority=1
    )
    Price.objects.create(
        product_id=35455,
        brand_id=2,
        price_list=4,
        start_date="2020-06-15T16:00:00Z",
        end_date="2020-12-31T23:59:59Z",
        price=39.95,
        priority=1
    )

    # Grupo 2: product_id 35455, brand_id 3
    Price.objects.create(
        product_id=35455,
        brand_id=3,
        price_list=1,
        start_date="2020-06-14T00:00:00Z",
        end_date="2020-12-31T23:59:59Z",
        price=37.50,
        priority=0
    )
    Price.objects.create(
        product_id=35455,
        brand_id=3,
        price_list=2,
        start_date="2020-06-14T15:00:00Z",
        end_date="2020-06-14T18:30:00Z",
        price=27.45,
        priority=1
    )
    Price.objects.create(
        product_id=35455,
        brand_id=3,
        price_list=3,
        start_date="2020-06-15T00:00:00Z",
        end_date="2020-06-15T11:00:00Z",
        price=32.50,
        priority=1
    )
    Price.objects.create(
        product_id=35455,
        brand_id=3,
        price_list=4,
        start_date="2020-06-15T16:00:00Z",
        end_date="2020-12-31T23:59:59Z",
        price=40.95,
        priority=1
    )

@pytest.mark.django_db
class TestNewPriceAPI:

    def setup_method(self):
        self.client = APIClient()

    def normalize_response(self, response):
        """Convierte las fechas a cadenas ISO para la comparación."""
        response.data['start_date'] = response.data['start_date'].isoformat()
        response.data['end_date'] = response.data['end_date'].isoformat()
        response.data['price'] = float(response.data['price'])  # Asegura que el precio esté en float
        return response.data

    # Test 1: 10:00 on 14th June (UTC) for brand_id 2
    def test_price_at_10_am_14th_june_brand_2(self, create_new_prices):
        application_date = datetime(2020, 6, 14, 10, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 2,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 2,
            "price_list": 1,
            "start_date": "2020-06-14T00:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 36.50
        }

    # Test 2: 16:00 on 14th June (UTC) for brand_id 3
    def test_price_at_16_pm_14th_june_brand_3(self, create_new_prices):
        application_date = datetime(2020, 6, 14, 16, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 3,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 3,
            "price_list": 2,
            "start_date": "2020-06-14T15:00:00+00:00",
            "end_date": "2020-06-14T18:30:00+00:00",
            "price": 27.45
        }

    # Test 3: 21:00 on 14th June (UTC) for brand_id 2
    def test_price_at_21_pm_14th_june_brand_2(self, create_new_prices):
        application_date = datetime(2020, 6, 14, 21, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 2,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 2,
            "price_list": 1,
            "start_date": "2020-06-14T00:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 36.50
        }

    # Test 4: 10:00 on 15th June (UTC) for brand_id 3
    def test_price_at_10_am_15th_june_brand_3(self, create_new_prices):
        application_date = datetime(2020, 6, 15, 10, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 3,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 3,
            "price_list": 3,
            "start_date": "2020-06-15T00:00:00+00:00",
            "end_date": "2020-06-15T11:00:00+00:00",
            "price": 32.50
        }

    # Test 5: 21:00 on 16th June (UTC) for brand_id 2
    def test_price_at_21_pm_16th_june_brand_2(self, create_new_prices):
        application_date = datetime(2020, 6, 16, 21, 0, 0, tzinfo=pytz.UTC)

        response = self.client.get(
            reverse('price-view'),
            {
                'product_id': 35455,
                'brand_id': 2,
                'application_date': application_date.isoformat()
            }
        )
        assert response.status_code == 200
        normalized_data = self.normalize_response(response)
        assert normalized_data == {
            "product_id": 35455,
            "brand_id": 2,
            "price_list": 4,
            "start_date": "2020-06-15T16:00:00+00:00",
            "end_date": "2020-12-31T23:59:59+00:00",
            "price": 39.95
        }
