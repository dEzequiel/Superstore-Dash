import requests
import pandas as pd

API_BASE_URL = "http://localhost:5000/api"

REGION_MAP = {
    'US': 'US',
    'APAC': 'APAC',
    'EU': 'EU',
    'LATAM': 'LATAM',
    'EMEA': 'EMEA',
    'AFRICA': 'Africa',
    'CANADA': 'Canada'
}

CATEGORY_MAP = {
    'TECH': 'Technology',
    'FURN': 'Furniture',
    'OFF': 'Office Supplies'
}

def fetch_targets():
    try:
        response = requests.get(f"{API_BASE_URL}/targets", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching targets from API: {e}")
        return None

def fetch_targets_by_region(region):
    try:
        response = requests.get(f"{API_BASE_URL}/targets/{region}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching targets for region {region}: {e}")
        return None

def parse_targets(api_response):
    if api_response is None:
        return pd.DataFrame()
    
    targets = api_response.get('sales_targets', [])
    if not targets:
        return pd.DataFrame()
    
    df = pd.DataFrame(targets)
    
    df['Market'] = df['region_code'].map(REGION_MAP)
    df['Category'] = df['product_line'].map(CATEGORY_MAP)
    df['Year'] = df['fiscal_year']
    df['Target'] = df['quarterly_target'] * 4
    df['GrowthExpected'] = df['growth_rate_expected']
    df['Priority'] = df['priority_level']
    
    return df[['Market', 'Category', 'Year', 'Target', 'GrowthExpected', 'Priority']]

def get_targets_df():
    raw_data = fetch_targets()
    return parse_targets(raw_data)

def calculate_target_achievement(sales_df, targets_df):
    if targets_df.empty:
        return None
    
    sales_df = sales_df.copy()
    sales_df['Year'] = sales_df['Order Date'].dt.year
    
    sales_by_market_cat_year = sales_df.groupby(['Market', 'Category', 'Year']).agg({
        'Sales': 'sum'
    }).reset_index()
    
    merged = sales_by_market_cat_year.merge(
        targets_df,
        on=['Market', 'Category', 'Year'],
        how='left'
    )
    
    merged['Achievement'] = (merged['Sales'] / merged['Target'] * 100).fillna(0)
    
    return merged

def get_overall_achievement(sales_df, targets_df):
    if targets_df.empty:
        return 0, 0, 0
    
    merged = calculate_target_achievement(sales_df, targets_df)
    if merged is None or merged.empty:
        return 0, 0, 0
    
    total_sales = merged['Sales'].sum()
    total_target = merged['Target'].sum()
    overall_pct = (total_sales / total_target * 100) if total_target > 0 else 0
    
    return total_sales, total_target, overall_pct

