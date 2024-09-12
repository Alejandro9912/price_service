# Price Service - Prueba Técnica para Desarrollador Junior

## Descripción del Proyecto

Este proyecto consiste en construir un servicio API REST que procesa datos de precios para una empresa de comercio electrónico. El servicio permite consultar los precios de los productos basándose en varios parámetros, incluidos el ID del producto, el ID de la marca y una fecha de aplicación, devolviendo el precio correspondiente. El servicio fue desarrollado utilizando Python y Django, con SQLite como base de datos en memoria para facilitar la configuración y pruebas rápidas.

## Enunciado del Problema

La base de datos de la empresa de comercio electrónico almacena información de precios en una tabla llamada **PRICES**, que refleja el precio final de venta (PVP) y la tarifa aplicable para un producto dentro de un rango de fechas. El desafío requería la construcción de un servicio que recuperara el precio correcto de un producto de una marca específica en un momento dado.

### Campos Clave:
- **BRAND_ID**: Clave foránea que representa la marca (1 = STORE_X).
- **START_DATE** & **END_DATE**: Rango de fechas durante el cual el precio es válido.
- **PRICE_LIST**: Identificador de la lista de precios aplicable.
- **PRODUCT_ID**: Identificador único del producto.
- **PRIORITY**: Resuelve conflictos de precios cuando dos entradas de precios se superponen. Cuanto mayor es el valor, mayor es la prioridad.
- **PRICE**: Precio final de venta del producto.
- **CURR**: Código de moneda en formato ISO.

### Requisitos:
- Un endpoint REST que acepte `application_date`, `product_id`, y `brand_id` como parámetros.
- El endpoint devuelve `product_id`, `brand_id`, `price_list`, el rango de fechas efectivo (`start_date`, `end_date`), y el precio final del producto.
- La aplicación fue construida usando Python y Django REST framework.

## Configuración del Proyecto

### Requisitos:
Para configurar y ejecutar el proyecto localmente, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.x
- Django 5.1.x
- Django REST framework
- Pytest para pruebas

### Instalación:

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/Alejandro9912/price_service.git
    ```

2. Navegar al directorio del proyecto:
    ```bash
    cd prices_services
    ```

3. Instalar las dependencias usando `pip`:
    ```bash
    pip install -r requirements.txt
    ```

4. Aplicar las migraciones:
    ```bash
    python manage.py migrate
    ```

5. Ejecutar el servidor de desarrollo de Django:
    ```bash
    python manage.py runserver
    ```

## Uso de la API REST

El servicio expone un único endpoint API para consultar los datos de precios:

GET /price-view/


#### Parámetros de Consulta:
- `application_date` : Fecha en la que el precio debe ser efectivo.
- `product_id`: ID del producto a consultar.
- `brand_id`: ID de la marca/tienda.

#### Ejemplo:
```bash
GET /price-view/?product_id=35455&brand_id=1&application_date=2020-06-14T10:00:00Z
```

```json
{
  "product_id": 35455,
  "brand_id": 1,
  "price_list": 1,
  "start_date": "2020-06-14T00:00:00+00:00",
  "end_date": "2020-12-31T23:59:59+00:00",
  "price": 35.50
}
```
## Pruebas

Para garantizar la funcionalidad del servicio, se implementaron varios casos de prueba utilizando `pytest`. Estas pruebas validan que se devuelvan los datos de precios correctos para varios escenarios.

### Casos de Prueba:

1. **Prueba 1**: Solicitud de precio a las 10:00 del 14 de junio para el producto 35455, marca 1.
2. **Prueba 2**: Solicitud de precio a las 16:00 del 14 de junio para el producto 35455, marca 1.
3. **Prueba 3**: Solicitud de precio a las 21:00 del 14 de junio para el producto 35455, marca 1.
4. **Prueba 4**: Solicitud de precio a las 10:00 del 15 de junio para el producto 35455, marca 1.
5. **Prueba 5**: Solicitud de precio a las 21:00 del 16 de junio para el producto 35455, marca 1.

### Ejecución de Pruebas:

Ejecuta el siguiente comando para ejecutar las pruebas:

```bash
pytest
```

## Consideraciones de Diseño

- **Django ORM**: Se utiliza el ORM de Django para interactuar con la base de datos SQLite, lo que facilita la validación de datos y la gestión de restricciones.
- **Validación Personalizada**: Se asegura que `start_date` sea anterior a `end_date` y que los precios no puedan ser negativos mediante validaciones tanto a nivel de base de datos como a nivel de aplicación.
- **Priorización**: El campo `priority` garantiza que, si dos precios se superponen en el tiempo, se seleccione el de mayor prioridad.

## Conclusión

Este proyecto demuestra la capacidad de construir un servicio API robusto que pueda manejar lógica compleja de precios. El uso de Django y SQLite permite un desarrollo rápido y pruebas sencillas, mientras que `pytest` asegura la calidad y corrección del código. El servicio está diseñado para ser escalable y adaptable a nuevos requisitos, como agregar soporte para más monedas o extender el modelo de precios.


