from dash import html, dcc

def create_content():
    return html.Main(
        className="content",
        children=[
            html.Section(
                className="kpi-section",
                children=[
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Ventas Totales", className="kpi-label"),
                            html.H3(id="kpi-sales", className="kpi-value"),
                            html.Span(id="kpi-sales-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Beneficio Total", className="kpi-label"),
                            html.H3(id="kpi-profit", className="kpi-value"),
                            html.Span(id="kpi-profit-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Pedidos", className="kpi-label"),
                            html.H3(id="kpi-orders", className="kpi-value"),
                            html.Span(id="kpi-orders-trend", className="kpi-trend")
                        ]
                    ),
                    html.Div(
                        className="kpi-card",
                        children=[
                            html.Span("Margen Beneficio", className="kpi-label"),
                            html.H3(id="kpi-margin", className="kpi-value"),
                            html.Span(id="kpi-margin-trend", className="kpi-trend")
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
                            dcc.Graph(
                                id="chart-sales-time",
                                className="chart",
                                style={'height': '500px'},
                            )
                        ]
                    ),
                ]
            ),
        ]
    )
