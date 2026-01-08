from dash import callback, Output, Input

def register_kpi_callbacks(df):
    @callback(
        [
            Output("kpi-sales", "children"),
            Output("kpi-profit", "children"),
            Output("kpi-orders", "children"),
            Output("kpi-margin", "children"),
        ],
        Input("url", "pathname")
    )
    def update_kpis(_):
        total_sales = df['Sales'].sum()
        total_profit = df['Profit'].sum()
        total_orders = df['Order ID'].nunique()
        margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
        
        return [
            f"${total_sales:,.0f}",
            f"${total_profit:,.0f}",
            f"{total_orders:,}",
            f"{margin:.1f}%"
        ]
