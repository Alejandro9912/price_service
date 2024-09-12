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

