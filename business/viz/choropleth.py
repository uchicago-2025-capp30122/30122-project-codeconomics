from dash import dcc, html
import geopandas as gpd
from ..analyze.business_outlook import get_macro_table
from .plots import create_choropleth
from .style import style_section_split

# Load Data Macro
df_macro = get_macro_table()
df_macro = df_macro[df_macro['crime_rate'] < 1000] # Removing Outlier

# Convert DataFrame to GeoDataFrame
gdf = gpd.GeoDataFrame(df_macro, geometry='polygon')

choropleths = html.Div(
                    children = [
                        html.Div(
                            children = [
                                html.H3("Some are optimistic!",
                                        style = {
                                                'text-align': 'left',
                                                'color': '#800000',
                                                'font-size': '30px',
                                                'font-family': 'Arial, sans-serif',
                                                'font-weight': 'bold',
                                                'max-width': '800px',
                                                'margin': '20px auto',
                                                'margin-top': '20px',
                                        }),
                                dcc.Graph(
                                        figure=create_choropleth(gdf, 'new_rate', 'New Business Rate by Zip Code (2024)'),
                                        style={"width": "100%", "height": "80vh", "display": "flex", "flex-direction": "column",
                                                       "margin-top": "50px"}
                                    )
                            ],
                            style = {"width": "50%", "height": "100vh"}),
                        html.Div(
                            children = [
                                html.H3("But, some are Unfortunate!",
                                        style = {
                                                'text-align': 'left',
                                                'color': '#800000',
                                                'font-size': '30px',
                                                'font-family': 'Arial, sans-serif',
                                                'font-weight': 'bold',
                                                'max-width': '800px',
                                                'margin': '20px auto',
                                                'margin-top': '20px',
                                        }),
                                dcc.Graph(
                                        figure=create_choropleth(gdf, 'closed_rate', 'Turnover Rate by Zip Code (2024)'),
                                        style={"width": "100%", "height": "80vh", "display": "flex", "flex-direction": "column",
                                                       "margin-top": "50px"}
                                    )
                            ],
                            style = {"width":"50%","height": "100vh"})                    
                    ],
                    style = style_section_split
                )