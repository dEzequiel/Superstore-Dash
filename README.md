# Superstore-Dash

## Resumen

Global Superstore es un minorista global en línea con sede en Nueva York, orientado a ser el destino integral para clientes de 147 países. Ofrece más de 10,000 productos en tres categorías principales: suministros de oficina (por ejemplo, grapas), muebles (por ejemplo, sillas) y tecnología (por ejemplo, smartphones).

## Explicación del dataset

- **Row ID**: Identificador único de la fila en la hoja de cálculo.
- **Order ID**: Identificador único de cada pedido realizado.
- **Order Date**: Fecha en que se realizó el pedido.
- **Ship Date**: Fecha de envío del pedido al cliente.
- **Ship Mode**: Método de envío utilizado para el pedido.
- **Customer ID**: Identificador único para cada cliente.
- **Customer Name**: Nombre del cliente o entidad que realiza el pedido.
- **Segment**: Segmento o categoría para clasificar pedidos.
- **City**: Ciudad asociada al pedido.
- **State**: Estado asociado al pedido.
- **Country**: País asociado al pedido.
- **Postal Code**: Código postal del cliente, útil para análisis geográficos y logísticos. *Nota: No todos los pedidos poseen este dato disponible.*
- **Market**: Región de mercado correspondiente al pedido (ej. US, APAC, EMEA).
- **Region**: Subdivisión geográfica, útil para análisis regionales.
- **Product ID**: Identificador único para cada producto.
- **Category**: Categoría general del producto.
- **Sub-Category**: Subcategoría específica dentro de la categoría principal.
- **Product Name**: Nombre o descripción del producto.
- **Sales**: Ingresos totales generados por el pedido (se calcula multiplicando cantidad y precio).
- **Quantity**: Cantidad de unidades del producto en el pedido.
- **Discount**: Descuento aplicado a productos o pedidos.
- **Profit**: Beneficio o pérdida neta asociada al pedido o producto.
- **Shipping Cost**: Coste total de envío del pedido.
- **Order Priority**: Prioridad asignada al pedido según criterios del negocio.

## Arrancar API y dashboard

Usa `python run_all.py` para arrancar simultáneamente la API de objetivos (`api/fake_api.py`) y el dashboard (`app.py`). El script se encarga de mantener ambos procesos y cancelas con `Ctrl+C`.

