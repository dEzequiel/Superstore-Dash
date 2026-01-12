from dash import callback, Output, Input
import pandas as pd
from io import StringIO
from src.data.api_client import get_targets_df, get_overall_achievement

def register_kpi_callbacks(df):
    @callback(
        [
            Output("kpi-sales", "children"),
            Output("kpi-profit", "children"),
            Output("kpi-orders", "children"),
            Output("kpi-margin", "children"),
            Output("kpi-ticket", "children"),
            Output("kpi-target", "children"),
            Output("kpi-card-target", "className"),
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
        
        targets_df = get_targets_df()
        _, _, achievement_pct = get_overall_achievement(df_filtered, targets_df)
        
        if achievement_pct > 0:
            if achievement_pct >= 100:
                card_class = "kpi-card kpi-card-api kpi-status-success"
            elif achievement_pct >= 80:
                card_class = "kpi-card kpi-card-api kpi-status-warning"
            else:
                card_class = "kpi-card kpi-card-api kpi-status-danger"
            target_value = f"{achievement_pct:.1f}%"
        else:
            target_value = "N/A"
            card_class = "kpi-card kpi-card-api"
        
        return [
            f"${total_sales:,.0f}",
            f"${total_profit:,.0f}",
            f"{total_orders:,}",
            f"{margin:.1f}%",
            f"${ticket:,.0f}",
            target_value,
            card_class
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
        
        targets_df = get_targets_df()
        sales_actual, target_total, achievement_pct = get_overall_achievement(df_filtered, targets_df)
        
        target_status = ""
        if achievement_pct > 0:
            if achievement_pct >= 100:
                target_status = f"**Objetivo superado** con un {achievement_pct:.1f}% de cumplimiento"
            elif achievement_pct >= 80:
                target_status = f"**Cerca del objetivo** con un {achievement_pct:.1f}% de cumplimiento"
            else:
                target_status = f"**Por debajo del objetivo** con un {achievement_pct:.1f}% de cumplimiento"
        
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
{f'- {target_status}' if target_status else ''}

*Utiliza los filtros de la barra lateral para explorar segmentos específicos del negocio.*
*Los datos de objetivos provienen de la API de targets (puerto 5000).*
"""
        return summary
