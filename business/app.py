from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pathlib
from business.analyze.business_outlook import calculate_changes_business
from business.viz.plots import create_scatter_plot
from business.viz.business_time_series import df_time_series, month_range, create_maps, business_time_series

path_data = pathlib.Path(__file__).parent.parent / 'business/data'

# Initialize the Dash app
app = Dash(__name__)

# Set random seed for reproducibility
np.random.seed(42)

# Load Data Scatter
df_scatter = pd.read_csv(path_data / 'dummy_scatter.csv')

# Styles
style_section_split =  {'height': '100vh', 
                        'padding': '20px', 
                        'display': 'flex', 
                        'justify-content': 'space-around'
                                }
style_scatter = {'width': '30%', 'display': 'inline-block', 'padding': '20px'}




intro_layout = html.Div(
                    children=[
                        html.H1(
                            children=[
                                "Blown Away:",
                                html.Br(),
                                "The Rise and Fall of Businesses in the Windy City"],
                            style={
                            'text-align': 'left',
                            'color': '#D9D9D9',
                            'font-size': '50px',
                            'font-family': 'Arial, sans-serif',
                            'font-weight': 'bold',
                            'max-width': '800px',
                            'margin': '30px auto',
                            'margin-top': '250px',
                        }),

                        html.P(
                            "Chicago's business landscape is constantly evolving, with new enterprises emerging while others shut their doors. "
                            "This project examines the patterns of business openings and closures in relation to key macroeconomic variables such as median income and crime rate. "
                            "By combining geospatial and statistical analysis, we aim to uncover insights into how economic conditions and public safety shape business activity in the Windy City.",
                            style={
                                'text-align': 'left',
                                'max-width': '800px',
                                'margin': '20px auto',
                                'font-size': '18px',
                                'font-family': 'Arial, sans-serif',
                                'color': 'white',
                                'margin-bottom': '400px'
                            }
                        )

                    ],
                    style={'height': '100vh',
                           'padding': '1px',
                           'background-color':'#800000'}
                )

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
                                html.P('Another GIS here - New Business')
                            ],
                            style = {}),
                        html.Div(
                            children = [
                                html.H3("Some are Unfortunate!",
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
                                html.P('Another GIS here - Turn Over rate')
                            ],
                            style = {})                    
                    ],
                    style = style_section_split
                )

scatters = html.Div(
                    children=[
                        
                        html.Div(
                            children=[
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter, 'med_income', 'newbiz_rate',
                                                                   x_axis_title='Median Income', y_axis_title='New Business (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter, 'crime_rate', 'newbiz_rate',
                                                                   x_axis_title='Crime Rate', y_axis_title='New Business (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter, 'theft_rate', 'newbiz_rate',
                                                                   x_axis_title='Theft Rate', y_axis_title='New Business (%Pop)')
                                        ),
                                    style = style_scatter
                                )
                            ],
                            style={'padding': '20px', 
                                   'display': 'flex', 
                                   'justify-content': 'space-around'}
                        ),

                        html.Div(
                            children=[
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter,'med_income', 'turnover_rate',
                                                                   x_axis_title='Median Income', y_axis_title='Turnover (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter,'crime_rate', 'turnover_rate',
                                                                   x_axis_title='Crime Rate', y_axis_title='Turnover (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_scatter,'theft_rate', 'turnover_rate',
                                                                   x_axis_title='Theft Rate', y_axis_title='Turnover (%Pop)')
                                    ),
                                    style = style_scatter
                                )
                            ],
                            style={'padding': '20px', 
                                   'display': 'flex', 
                                   'justify-content': 'space-around'}
                        ),
                    ],

                    style={'height': '100vh',
                           'padding': '20px'}
                )

app.layout = html.Div(
    children=[
        intro_layout,
        business_time_series,
        choropleths,
        scatters
    ],
    style={'background-color': '#fff', 'height': '100%', 'font-family': 'Arial, sans-serif'}
)

# Callback to update the map based on the selected month
@app.callback(
    Output("business-map", "figure"),
    [Input("month-slider", "value")],
)
def update_map(selected_month_index):
    selected_month = month_range[selected_month_index]  # Convert index to actual month (Period)

    filtered_df = df_time_series
    # Assign colors based on whether the business is still running
    filtered_df["operate"] = filtered_df["final_date"].dt.to_period("M").apply(
        lambda x: "Running" if x >= selected_month else "Stopped"
    )

    filtered_df = filtered_df.sort_values("operate")  # Sort to ensure "Stopped" comes last

    return create_maps(filtered_df, selected_month)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
