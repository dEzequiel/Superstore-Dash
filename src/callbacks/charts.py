from dash import callback, Output, Input
import plotly.graph_objects as go

def register_chart_callbacks(df):
    @callback(
        Output("chart-sales-time", "figure"),
        Input("url", "pathname")
    )
    def update_sales_time_chart(_):
        df_monthly = df.groupby(df['Order Date'].dt.to_period('M')).agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index()
        df_monthly['Order Date'] = df_monthly['Order Date'].astype(str)
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df_monthly['Order Date'],
            y=df_monthly['Sales'],
            name='Ventas',
            mode='lines+markers',
            line=dict(color='#ed8936', width=2),
            marker=dict(size=6),
            hovertemplate='%{x}<br>Ventas: $%{y:,.0f}<extra></extra>'
        ))
        
        fig.add_trace(go.Scatter(
            x=df_monthly['Order Date'],
            y=df_monthly['Profit'],
            name='Beneficio',
            mode='lines+markers',
            line=dict(color='#38a169', width=2),
            marker=dict(size=6),
            hovertemplate='%{x}<br>Beneficio: $%{y:,.0f}<extra></extra>'
        ))
        
        fig.update_layout(
            height=500,
            autosize=True,
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e2e8f0'),
            hovermode='x unified',
            hoverlabel=dict(
                bgcolor='#1e293b',
                font_color='#e2e8f0',
                bordercolor='#334155'
            ),
            legend=dict(
                orientation='h',
                yanchor='bottom',
                y=1.02,
                xanchor='right',
                x=1,
                font=dict(size=12)
            ),
            margin=dict(l=60, r=20, t=40, b=60),
            xaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                tickangle=-45,
                dtick='M3',
            ),
            yaxis=dict(
                showgrid=True,
                gridcolor='rgba(255,255,255,0.1)',
                tickprefix='$',
                tickformat=',.0f'
            )
        )
        
        return fig
