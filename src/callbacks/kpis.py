from dash import callback, Output, Input
import pandas as pd
from io import StringIO

def register_kpi_callbacks(df):
    @callback(
        [
            Output("kpi-sales", "children"),
            Output("kpi-profit", "children"),
            Output("kpi-orders", "children"),
            Output("kpi-margin", "children"),
            Output("kpi-ticket", "children")
        ],
        Input("filtered-data-store", "data")
    )
    def update_kpis(json_data):
        if json_data is None:
            df_filtered = df
        else:
            df_filtered = pd.read_json(StringIO(json_data), orient='split')
            df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'])
        
        total_sales = df_filtered['Sales'].sum()
        total_profit = df_filtered['Profit'].sum()
        total_orders = df_filtered['Order ID'].nunique()
        margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
        ticket = total_sales / total_orders if total_orders > 0 else 0
        
        return [
            f"${total_sales:,.0f}",
            f"${total_profit:,.0f}",
            f"{total_orders:,}",
            f"{margin:.1f}%",
            f"${ticket:,.0f}"
        ]
    
    @callback(
        Output("executive-summary", "children"),
        Input("filtered-data-store", "data")
    )
    def update_summary(json_data):
        if json_data is None:
            df_filtered = df
        else:
            df_filtered = pd.read_json(StringIO(json_data), orient='split')
            df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'])
        
        total_sales = df_filtered['Sales'].sum()
        total_profit = df_filtered['Profit'].sum()
        total_orders = df_filtered['Order ID'].nunique()
        num_customers = df_filtered['Customer ID'].nunique()
        num_products = df_filtered['Product ID'].nunique()
        avg_order_value = total_sales / total_orders if total_orders > 0 else 0
        margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
        
        top_category = df_filtered.groupby('Category')['Sales'].sum().idxmax()
        top_market = df_filtered.groupby('Market')['Sales'].sum().idxmax()
        
        summary = f"""
            ### Análisis Global Superstore

            **Período analizado:** {len(df_filtered):,} pedidos de {num_customers:,} clientes únicos

            **Métricas clave:**
            - **Ventas totales:** ${total_sales:,.0f}
            - **Beneficio neto:** ${total_profit:,.0f} (Margen: {margin:.1f}%)
            - **Valor promedio por pedido:** ${avg_order_value:,.0f}
            - **Productos diferentes:** {num_products:,}

            **Insights principales:**
            - La categoría con mayor volumen de ventas es **{top_category}**
            - El mercado más rentable es **{top_market}**
            - Se gestionaron **{total_orders:,}** pedidos en el período seleccionado

            *Utiliza los filtros de la barra lateral para explorar segmentos específicos del negocio.*
            """
        return summary
