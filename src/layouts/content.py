from dash import html, dcc

def create_content():
    return html.Main(
        className="content",
        children=[
            html.Section(
                className="info-section",
                children=[
                    dcc.Markdown("""
                    **Global Superstore** es una tienda online global con sede en Nueva York. Cuenta con un amplio catálogo de productos y 
                    su objetivo es ofrecer una solución integral para sus clientes a nivel mundial. Su clientela, procedente de 147 países,
                     puede explorar una oferta ilimitada de más de **10 000 productos**. Esta amplia selección se compone de tres categorías principales: 
                     **material de oficina** (p. ej., artículos básicos), **mobiliario** (p. ej., sillas) y **tecnología** (p. ej., smartphones).

                     **Al final del dashboard podrás encontrar un resumen ejecutivo que te permitirá obtener insights sobre el negocio.**
""", className="info-text")
                ]
            ),
            
            html.Section(
                className="kpi-section",
                children=[
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Ventas Totales", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=html.H3(id="kpi-sales", className="kpi-value")
                            ),
                            html.Span(id="kpi-sales-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Beneficio Total", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=html.H3(id="kpi-profit", className="kpi-value")
                            ),
                            html.Span(id="kpi-profit-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Pedidos", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=html.H3(id="kpi-orders", className="kpi-value")
                            ),
                            html.Span(id="kpi-orders-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Margen Beneficio", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=html.H3(id="kpi-margin", className="kpi-value")
                            ),
                            html.Span(id="kpi-margin-trend", className="kpi-trend")
                        ]
                    )
                    ,
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Ticket Medio", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=html.H3(id="kpi-ticket", className="kpi-value")
                            ),
                            html.Span(id="kpi-ticket-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        id="kpi-card-target",
                        className="kpi-card kpi-card-api",
                        children=[
                            html.Span("Objetivo Cumplido", className="kpi-label"),
                            dcc.Loading(
                                type="dot",
                                color="#22c55e",
                                children=html.H3(id="kpi-target", className="kpi-value")
                            ),
                            html.Span("(desde API)", className="kpi-source")
                        ]
                    )
                ]
            ),
            
            html.Section(
                className="charts-section",
                children=[
                    html.Div(
                        className="chart-container chart-large",
                        children=[
                            html.H3("Evolución de Ventas y Beneficios", className="chart-title"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=dcc.Graph(
                                    id="chart-sales-time",
                                    className="chart",
                                    style={'height': '450px'},
                                )
                            )
                        ]
                    ),
                ]
            ),
            
            html.Section(
                className="charts-section charts-grid",
                children=[
                    html.Div(
                        className="chart-container",
                        children=[
                            html.H3("Ventas por Categoría", className="chart-title"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=dcc.Graph(
                                    id="chart-category",
                                    className="chart",
                                    style={'height': '350px'}
                                )
                            )
                        ]
                    ),
                    html.Div(
                        className="chart-container",
                        children=[
                            html.H3("Ventas por Mercado", className="chart-title"),
                            dcc.Loading(
                                type="dot",
                                color="#3b82f6",
                                children=dcc.Graph(
                                    id="chart-market",
                                    className="chart",
                                    style={'height': '350px'}
                                )
                            )
                        ]
                    )
                ]
            ),
            
            html.Section(
                className="summary-section",
                children=[
                    dcc.Loading(
                        type="dot",
                        color="#3b82f6",
                        children=dcc.Markdown(id="executive-summary", className="summary-text")
                    )
                ]
            ),
        ]
    )
