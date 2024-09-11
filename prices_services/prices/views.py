from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Price
from django.utils.dateparse import parse_datetime
from django.http import Http404
import pytz

class PriceView(APIView):
    def get(self, request, *args, **kwargs):
        
        # Obtener parámetros de la URL
        product_id = request.query_params.get('product_id')
        brand_id = request.query_params.get('brand_id')
        application_date = request.query_params.get('application_date')

        # Validar que los parámetros estén presentes
        if not product_id or not brand_id or not application_date:
            return Response({"error": "Missing parameters"}, status=400)

        # Parsear la fecha de aplicación
        application_date = parse_datetime(application_date)
        if not application_date:
            return Response({"error": "Invalid date format"}, status=400)

        # Asegúrate de que 'application_date' es timezone-aware (con zona horaria)
        if application_date.tzinfo is None:
            application_date = application_date.replace(tzinfo=pytz.UTC)

        # Buscar los precios aplicables en la base de datos ordenados por prioridad
        prices = Price.objects.filter(
            product_id=int(product_id),  # Asegurar que el product_id sea entero
            brand_id=int(brand_id),  # Asegurar que el brand_id sea entero
            start_date__lte=application_date,
            end_date__gte=application_date
        ).order_by('-priority')  # Ordenamos de mayor a menor prioridad

        # Si no se encuentra ningún precio aplicable
        if not prices.exists():
            raise Http404("No price found")

        # Tomar el precio con mayor prioridad (primero de la lista ordenada)
        highest_priority_price = prices.first()

        # Devolver solo los campos solicitados en la prueba técnica
        result = {
            "product_id": highest_priority_price.product_id,
            "brand_id": highest_priority_price.brand_id,
            "price_list": highest_priority_price.price_list,  # Tarifa a aplicar
            "start_date": highest_priority_price.start_date,
            "end_date": highest_priority_price.end_date,
            "price": highest_priority_price.price  # Precio final
        }

        return Response(result)
