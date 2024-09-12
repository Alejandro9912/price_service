from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Price
from django.utils.dateparse import parse_datetime
from django.http import Http404
import pytz

class PriceView(APIView):
    """Vista para gestionar los precios según la marca, producto y fecha de aplicación."""

    def get(self, request, *args, **kwargs):
        # Obtener parámetros de la URL
        product_id = request.query_params.get('product_id')
        brand_id = request.query_params.get('brand_id')
        application_date = request.query_params.get('application_date')

        # Valida que los parámetros estén presentes
        if not product_id or not brand_id or not application_date:
            return Response({"error": "Missing parameters"}, status=400)

        # Parsea la fecha de aplicación
        application_date = parse_datetime(application_date)
        if not application_date:
            return Response({"error": "Invalid date format"}, status=400)

        # Asegurar de que la fecha tenga zona horaria
        if application_date.tzinfo is None:
            application_date = application_date.replace(tzinfo=pytz.UTC)

        # Buscar precios por producto y marca, ordenados por prioridad
        prices = Price.objects.filter(
            product_id=int(product_id),
            brand_id=int(brand_id),
            start_date__lte=application_date,
            end_date__gte=application_date
        ).order_by('-priority')

        if not prices.exists():
            raise Http404("No price found")

        highest_priority_price = prices.first()

        # Formato de la respuesta
        result = {
            "product_id": highest_priority_price.product_id,
            "brand_id": highest_priority_price.brand_id,
            "price_list": highest_priority_price.price_list,
            "start_date": highest_priority_price.start_date,
            "end_date": highest_priority_price.end_date,
            "price": highest_priority_price.price,
        }

        return Response(result)
