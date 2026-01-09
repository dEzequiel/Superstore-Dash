from dash import callback, Output, Input
import plotly.graph_objects as go
import pandas as pd
from io import StringIO

COLORS = {
    'primary': '#3b82f6',
    'secondary': '#64748b', 
    'success': '#22c55e',
    'text': '#e2e8f0',
    'muted': '#64748b',
    'grid': 'rgba(255,255,255,0.05)',
    'bg': '#1e293b',
    'border': '#2d3748'
}

def get_base_layout(height=400):
    return dict(
        height=height,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color=COLORS['muted'], size=11),
        hoverlabel=dict(
            bgcolor=COLORS['bg'],
            font_color=COLORS['text'],
            bordercolor=COLORS['border']
        ),
        margin=dict(l=50, r=20, t=20, b=40),
        xaxis=dict(
            showgrid=True,
            gridcolor=COLORS['grid'],
            zeroline=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLORS['grid'],
            zeroline=False
        )
    )

def register_chart_callbacks(df):
    @callback(
        Output("chart-sales-time", "figure"),
        Input("filtered-data-store", "data")
    )
    def update_sales_time_chart(json_data):
        if json_data is None:
            df_filtered = df
        else:
            df_filtered = pd.read_json(StringIO(json_data), orient='split')
            df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'])
        
        df_monthly = df_filtered.groupby(df_filtered['Order Date'].dt.to_period('M')).agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index()
        df_monthly['Order Date'] = df_monthly['Order Date'].astype(str)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df_monthly['Order Date'],
            y=df_monthly['Sales'],
            name='Ventas',
            mode='lines',
            line=dict(color=COLORS['primary'], width=2),
            hovertemplate='%{x}<br>Ventas: $%{y:,.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=df_monthly['Order Date'],
            y=df_monthly['Profit'],
            name='Beneficio',
            mode='lines',
            line=dict(color=COLORS['success'], width=2),
            hovertemplate='%{x}<br>Beneficio: $%{y:,.0f}<extra></extra>'
        ))
        
        layout = get_base_layout(450)
        layout.update(
            hovermode='x unified',
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1,
                font=dict(size=11, color=COLORS['muted'])
            ),
            margin=dict(l=60, r=20, t=30, b=50),
            xaxis=dict(
                showgrid=True,
                gridcolor=COLORS['grid'],
                tickangle=-45,
                dtick='M3',
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor=COLORS['grid'],
                tickprefix='$',
                tickformat=',.0f'
            )
        )
        fig.update_layout(layout)
        
        return fig
    
    @callback(
        Output("chart-category", "figure"),
        Input("filtered-data-store", "data")
    )
    def update_category_chart(json_data):
        if json_data is None:
            df_filtered = df
        else:
            df_filtered = pd.read_json(StringIO(json_data), orient='split')
            df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'])
        
        category_data = df_filtered.groupby('Category').agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index().sort_values('Sales', ascending=True)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=category_data['Sales'],
            y=category_data['Category'],
            orientation='h',
            marker=dict(color=COLORS['primary']),
            text=category_data['Sales'].apply(lambda x: f'${x:,.0f}'),
            textposition='auto',
            textfont=dict(color=COLORS['text'], size=11),
            hovertemplate='<b>%{y}</b><br>Ventas: $%{x:,.0f}<extra></extra>'
        ))
        
        layout = get_base_layout(350)
        layout.update(
            margin=dict(l=100, r=20, t=10, b=30),
            xaxis=dict(
                showgrid=True,
                gridcolor=COLORS['grid'],
                tickprefix='$',
                tickformat=',.0f'
            ),
            yaxis=dict(showgrid=False)
        )
        fig.update_layout(layout)
        
        return fig
    
    @callback(
        Output("chart-market", "figure"),
        Input("filtered-data-store", "data")
    )
    def update_market_chart(json_data):
        if json_data is None:
            df_filtered = df
        else:
            df_filtered = pd.read_json(StringIO(json_data), orient='split')
            df_filtered['Order Date'] = pd.to_datetime(df_filtered['Order Date'])
        
        market_data = df_filtered.groupby('Market').agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index().sort_values('Sales', ascending=False)
        
        fig = go.Figure()
        
        fig.add_trace(go.Bar(
            x=market_data['Market'],
            y=market_data['Sales'],
            marker=dict(color=COLORS['primary']),
            text=market_data['Sales'].apply(lambda x: f'${x:,.0f}'),
            textposition='outside',
            textfont=dict(color=COLORS['muted'], size=10),
            hovertemplate='<b>%{x}</b><br>Ventas: $%{y:,.0f}<extra></extra>'
        ))
        
        layout = get_base_layout(350)
        layout.update(
            margin=dict(l=50, r=20, t=30, b=40),
            xaxis=dict(showgrid=False),
            yaxis=dict(
                showgrid=True,
                gridcolor=COLORS['grid'],
                tickprefix='$',
                tickformat=',.0f'
            )
        )
        fig.update_layout(layout)
        
        return fig
