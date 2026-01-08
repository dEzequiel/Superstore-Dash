from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
import sys
sys.path.insert(0, '.')

from src.layouts import create_layout
from src.callbacks import register_navigation_callbacks, register_kpi_callbacks, register_chart_callbacks

df = pd.read_csv('./data/GlobalSuperstore-Data.csv')

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df['Sales'] = df['Sales'].astype(str).str.replace('$', '').str.replace(',', '').str.strip()
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

df['Profit'] = df['Profit'].astype(str).str.replace('$', '').str.replace(',', '').str.strip()
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')

df['Shipping Cost'] = df['Shipping Cost'].astype(str).str.replace('$', '').str.replace(',', '').str.strip()
df['Shipping Cost'] = pd.to_numeric(df['Shipping Cost'], errors='coerce')

# Inicializar la aplicación
app = Dash(__name__)
app.title = "Global Superstore Dashboard"

# Configurar el layout
app.layout = create_layout(df)

# Registrar callbacks
register_navigation_callbacks()
register_kpi_callbacks(df)
register_chart_callbacks(df)

if __name__ == '__main__':
    app.run(debug=True)
