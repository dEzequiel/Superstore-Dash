## Preguntas y respuestas

**¿Cuál es el objetivo o la pregunta que la visualización debe responder?**

El dashboard tiene como objetivo responder: ¿Cómo está evolucionando el rendimiento comercial de Global Superstore? Específicamente, permite analizar ventas, beneficios, márgenes y cumplimiento de objetivos a través de diferentes mercados, categorías y segmentos de clientes, identificando tendencias temporales y patrones de desempeño.

**¿Quién es la audiencia a la que la visualización debe dirigirse?**

La audiencia principal son gerentes y analistas de negocio de Global Superstore que necesitan monitorear KPIs comerciales, evaluar el cumplimiento de objetivos y tomar decisiones estratégicas basadas en datos de ventas globales.

**¿Qué tipo de información es necesario mostrar para alcanzar el objetivo?**

- **KPIs principales**: Ventas totales, beneficio total, número de pedidos, margen de beneficio, ticket medio y porcentaje de cumplimiento de objetivos (desde API)
- **Evolución temporal**: Tendencias de ventas y beneficios a lo largo del tiempo (mensuales)
- **Distribución por segmentos**: Ventas por categoría de producto y por mercado geográfico
- **Resumen ejecutivo**: Insights agregados con métricas clave y análisis contextual

**Para cada visualización, ¿se analiza una sola variable o una combinación de dos o más variables?**

- **Gráfico de evolución temporal**: Combina dos variables (Ventas y Beneficio) en función del tiempo (tres variables en total: tiempo, ventas, beneficio)
- **Gráfico de categorías**: Una variable principal (Ventas) agrupada por categoría de producto (dos variables)
- **Gráfico de mercados**: Una variable principal (Ventas) agrupada por mercado geográfico (dos variables)
- **KPIs**: Variables calculadas individuales pero derivadas de múltiples campos del dataset

**¿Se trata de variables continuas o categóricas?**

- **Continuas**: Sales, Profit, Shipping Cost, Order Date, Quantity (métricas numéricas)
- **Categóricas**: Market, Category, Sub-Category, Segment, Ship Mode, Order Priority (dimensiones de agrupación)
- **Mixtas**: Los gráficos combinan variables continuas (valores) con categóricas (dimensiones de agrupación)

**¿Qué tipo de visualización (layout) es el más adecuado para transmitir el mensaje o facilitar la exploración?**

El dashboard utiliza un **layout vertical con estructura de tarjetas** que incluye:
- **KPI cards**: Visualización clara y destacada de métricas clave en la parte superior (diseño de 6 tarjetas)
- **Gráfico de líneas temporal**: Para mostrar evolución de dos series (ventas y beneficios) a lo largo del tiempo
- **Gráficos de barras**: Horizontales para categorías (facilita lectura de etiquetas) y verticales para mercados (comparación directa)
- **Panel lateral de filtros**: Separado del contenido principal para no interferir con las visualizaciones
- **Resumen ejecutivo en texto**: Al final del dashboard para proporcionar contexto narrativo

**¿Cómo se proporcionará al usuario una vista general de los datos (Overview first)?**

La vista general se proporciona mediante:
1. **KPIs destacados** en la parte superior que resumen el estado general del negocio con 6 métricas clave
2. **Gráfico de evolución temporal** que muestra el panorama completo de ventas y beneficios mensuales
3. **Texto introductorio** que contextualiza el negocio de Global Superstore
4. **Resumen ejecutivo** al final que sintetiza los insights principales del período analizado
5. Por defecto, el dashboard muestra **todos los datos** sin filtros aplicados, ofreciendo la vista más amplia

**¿Qué operaciones permitirán al usuario hacer zoom o aplicar filtros a los datos?**

El usuario puede filtrar los datos mediante:
- **Rango de fechas**: DatePickerRange para seleccionar períodos específicos de análisis
- **Mercado**: Dropdown multi-selección para filtrar por regiones geográficas (US, APAC, EU, EMEA, Africa, Canada, LATAM)
- **Categoría**: Dropdown multi-selección para filtrar por tipo de producto (Furniture, Office Supplies, Technology)
- **Segmento**: Dropdown multi-selección para filtrar por tipo de cliente (Consumer, Corporate, Home Office)
- **Botón de reset**: Permite volver rápidamente a la vista completa sin filtros
- Todos los filtros son reactivos y actualizan simultáneamente los KPIs, gráficos y resumen ejecutivo

**¿Qué detalles específicos estarán disponibles para el usuario "bajo demanda" (Details on Demand)?**

- **Tooltips interactivos** en todos los gráficos que muestran valores exactos al pasar el cursor (hover)
- **Valores formateados** en las barras de los gráficos de categoría y mercado
- **Hover unificado** en el gráfico temporal que muestra ventas y beneficios simultáneamente para cada mes
- **Resumen ejecutivo dinámico** que se actualiza con los filtros aplicados, mostrando:
  - Número exacto de pedidos y clientes únicos
  - Métricas financieras precisas (ventas, beneficio, margen)
  - Categoría y mercado más rentables en el segmento filtrado
  - Estado de cumplimiento de objetivos con porcentaje exacto
- **KPI de objetivos desde API** que proporciona datos en tiempo real del cumplimiento de metas
