from dash import html, dcc

NAV_LINKS = [
    {"label": "Dashboard", "href": "/"},
    {"label": "Ventas", "href": "/ventas"},
    {"label": "Productos", "href": "/productos"},
    {"label": "Clientes", "href": "/clientes"},
]

def create_header():
    return html.Header(
        className="header",
        children=[
            html.Div(
                className="header-brand",
                children=[
                    html.Img(src="/assets/logo.svg", className="header-logo"),
                    html.H1("Global Superstore", className="header-title"),
                ]
            ),
            html.Nav(
                id="header-nav",
                className="header-nav",
                children=[
                    html.A(
                        link["label"],
                        href=link["href"],
                        id=f"nav-link-{link['href'].strip('/') or 'home'}",
                        className="nav-link"
                    )
                    for link in NAV_LINKS
                ]
            ),
            html.Div(
                className="header-info",
                children=[
                    html.Span("by Ezequiel Dlr", className="header-author"),
                ]
            )
        ]
    )

