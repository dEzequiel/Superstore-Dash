from dash import callback, Output, Input
import pandas as pd

def register_filter_callbacks(df):
    markets = sorted(df['Market'].unique())
    categories = sorted(df['Category'].unique())
    segments = sorted(df['Segment'].unique())
    min_date = df['Order Date'].min()
    max_date = df['Order Date'].max()
    
    @callback(
        Output('filtered-data-store', 'data'),
        [
            Input('filter-date-range', 'start_date'),
            Input('filter-date-range', 'end_date'),
            Input('filter-market', 'value'),
            Input('filter-category', 'value'),
            Input('filter-segment', 'value'),
        ]
    )
    def filter_data(start_date, end_date, selected_markets, selected_categories, selected_segments):
        filtered_df = df.copy()
        
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df['Order Date'] >= start_date) &
                (filtered_df['Order Date'] <= end_date)
            ]
        
        if selected_markets and len(selected_markets) > 0:
            filtered_df = filtered_df[filtered_df['Market'].isin(selected_markets)]
        
        if selected_categories and len(selected_categories) > 0:
            filtered_df = filtered_df[filtered_df['Category'].isin(selected_categories)]
        
        if selected_segments and len(selected_segments) > 0:
            filtered_df = filtered_df[filtered_df['Segment'].isin(selected_segments)]
        
        return filtered_df.to_json(date_format='iso', orient='split')
    
    @callback(
        [
            Output('filter-date-range', 'start_date'),
            Output('filter-date-range', 'end_date'),
            Output('filter-market', 'value'),
            Output('filter-category', 'value'),
            Output('filter-segment', 'value'),
        ],
        Input('btn-reset-filters', 'n_clicks'),
        prevent_initial_call=True
    )
    def reset_filters(n_clicks):
        return [
            min_date,
            max_date,
            markets,
            categories,
            segments
        ]

