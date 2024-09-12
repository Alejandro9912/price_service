from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

class Price(models.Model):
    # Definición de los campos principales del modelo

    # ID del producto, debe ser un valor positivo
    product_id = models.PositiveIntegerField()  # Asegura que sea un valor positivo
    
    # ID de la marca, debe ser un valor positivo
    brand_id = models.PositiveIntegerField()    # Asegura que sea un valor positivo
    
    # Lista de precios, debe ser un valor positivo
    price_list = models.PositiveIntegerField()  # Asegura que sea un valor positivo
    
    # Fecha de inicio del periodo en que el precio es válido
    start_date = models.DateTimeField()         # Fecha de inicio de la vigencia del precio
    
    # Fecha de fin del periodo en que el precio es válido
    end_date = models.DateTimeField()           # Fecha de finalización de la vigencia del precio
    
    # Precio del producto, debe ser positivo o cero, con hasta 10 dígitos y 2 decimales
    price = models.DecimalField(
        max_digits=10,                         # Limita el número total de dígitos a 10
        decimal_places=2,                      # Limita los decimales a 2 dígitos
        validators=[MinValueValidator(0.0)]    # El precio debe ser positivo o cero
    )
    
    # Campo para la moneda, con un máximo de 3 caracteres (ej. USD, EUR)
    curr = models.CharField(
        max_length=3,                          # Limita la longitud a 3 caracteres (ISO 4217)
        default='USD'                          # Valor por defecto 'USD' si no se especifica
    )

    # Definición de las opciones para la prioridad
    PRIORITY_CHOICES = [
        (0, 'Baja'),   # Prioridad baja
        (1, 'Alta'),   # Prioridad alta
    ]
    
    # Campo de prioridad que usa opciones limitadas y un valor predeterminado de 0 (baja)
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES, default=0)  # Usa choices para valores predefinidos

    # Metadatos del modelo
    class Meta:
        # Define restricciones de unicidad y validaciones en la base de datos
        constraints = [
            models.UniqueConstraint(
                fields=['product_id', 'brand_id', 'price_list'],  # La combinación de estos campos debe ser única
                name='unique_price_for_brand_and_list'            # Nombre de la restricción de unicidad
            ),
            models.CheckConstraint(
                condition=models.Q(price__gte=0),  # Verifica que el precio sea mayor o igual a 0
                name='price_positive'              # Nombre de la restricción de verificación
            ),
            models.CheckConstraint(
                condition=models.Q(start_date__lt=models.F('end_date')),  # Verifica que la fecha de inicio sea menor que la fecha de fin
                name='valid_date_range'            # Nombre de la restricción de verificación para fechas válidas
            ),
        ]

        # Define índices para mejorar el rendimiento de consultas en los campos product_id, brand_id y price_list
        indexes = [
            models.Index(fields=['product_id', 'brand_id', 'price_list']),
        ]

    # Validaciones personalizadas en el nivel de aplicación
    def clean(self):
        # Valida que la fecha de inicio sea anterior a la fecha de fin
        if self.start_date >= self.end_date:
            raise ValidationError('La fecha de inicio debe ser anterior a la fecha de fin.')

        # Valida que el precio no sea negativo
        if self.price < 0:
            raise ValidationError('El precio no puede ser negativo.')

    # Representación en cadena del objeto para mostrar información útil cuando se imprima o se consulte
    def __str__(self):
        return f"Price {self.product_id} for brand {self.brand_id}, Price List {self.price_list}, Priority {self.priority}, Currency {self.curr}"
