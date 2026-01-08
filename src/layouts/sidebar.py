from dash import html, dcc

def create_sidebar(df):
    markets = sorted(df['Market'].unique())
    categories = sorted(df['Category'].unique())
    segments = sorted(df['Segment'].unique())
    min_date = df['Order Date'].min()
    max_date = df['Order Date'].max()
    
    return html.Aside(
        className="sidebar",
        children=[
            html.H2("Filtros", className="sidebar-title"),
            
            html.Div(
                className="filter-group",
                children=[
                    html.Label("Rango de Fechas", className="filter-label"),
                    dcc.DatePickerRange(
                        id='filter-date-range',
                        min_date_allowed=min_date,
                        max_date_allowed=max_date,
                        start_date=min_date,
                        end_date=max_date,
                        display_format='DD/MM/YYYY',
                        className="filter-datepicker"
                    )
                ]
            ),
            
            html.Div(
                className="filter-group",
                children=[
                    html.Label("Mercado", className="filter-label"),
                    dcc.Dropdown(
                        id='filter-market',
                        options=[{'label': m, 'value': m} for m in markets],
                        value=markets,
                        multi=True,
                        placeholder="Seleccionar mercados...",
                        className="filter-dropdown"
                    )
                ]
            ),
            
            html.Div(
                className="filter-group",
                children=[
                    html.Label("Categoría", className="filter-label"),
                    dcc.Dropdown(
                        id='filter-category',
                        options=[{'label': c, 'value': c} for c in categories],
                        value=categories,
                        multi=True,
                        placeholder="Seleccionar categorías...",
                        className="filter-dropdown"
                    )
                ]
            ),
            
            html.Div(
                className="filter-group",
                children=[
                    html.Label("Segmento", className="filter-label"),
                    dcc.Dropdown(
                        id='filter-segment',
                        options=[{'label': s, 'value': s} for s in segments],
                        value=segments,
                        multi=True,
                        placeholder="Seleccionar segmentos...",
                        className="filter-dropdown"
                    )
                ]
            ),
            
            html.Button(
                "Resetear Filtros",
                id='btn-reset-filters',
                className="btn-reset"
            )
        ]
    )
