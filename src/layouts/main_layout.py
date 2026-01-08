from dash import html, dcc
from .header import create_header
from .sidebar import create_sidebar
from .content import create_content

def create_layout(df):
    return html.Div(
        className="app-container",
        children=[
            dcc.Store(id='filtered-data-store'),
            dcc.Location(id='url', refresh=False),
            
            create_header(),
            
            html.Div(
                className="main-container",
                children=[
                    create_sidebar(df),
                    create_content()
                ]
            ),
            
            html.Footer(
                className="footer",
                children=[
                    html.P("© 2024 Global Superstore Dashboard - Ezequiel Dlr"),
                    html.P("Datos: Global Superstore Dataset")
                ]
            )
        ]
    )
