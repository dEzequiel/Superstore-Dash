from dash import callback, Output, Input
from src.layouts.header import NAV_LINKS

def register_navigation_callbacks():
    outputs = [
        Output(f"nav-link-{link['href'].strip('/') or 'home'}", "className")
        for link in NAV_LINKS
    ]
    
    @callback(outputs, Input("url", "pathname"))
    def update_active_nav(pathname):
        if pathname is None:
            pathname = "/"
        
        return [
            "nav-link active" if pathname == link["href"] else "nav-link"
            for link in NAV_LINKS
        ]
