from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np
import pathlib
from business.viz.plots import create_scatter_plot

path_data = pathlib.Path(__file__).parent.parent / 'business/data'

# Initialize the Dash app
app = Dash(__name__)

# Set random seed for reproducibility
np.random.seed(42)

df_scatter = pd.read_csv(path_data / 'dummy_scatter.csv')


style_section_split =  {'height': '100vh', 
                        'padding': '20px', 
                        'display': 'flex', 
                        'justify-content': 'space-around'
                                }

style_scatter = {'width': '30%', 'display': 'inline-block', 'padding': '20px'}
# Layout with GIF and dropdown for filtering Plot 1

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

text_gis = "From 2019 to 2024, Chicago’s business landscape has seen businesses come and go, ebbing and flowing like the tides. Some thrived, while others faded away, leaving behind a changing cityscape. This evolution is not just numbers, but a story told through locations, each point on the map representing the rise and fall of a business in the heart of the city. Through GIS visualizations, we can track these shifts across neighborhoods—new businesses emerging and others disappearing, often influenced by factors like income levels and crime rates. The map reveals how the city's economy has grown and contracted in specific areas, reflecting both opportunities and challenges faced by entrepreneurs. As you explore this data, one question remains: Can you see a pattern? Is there a spatial connection between business success and the surrounding environment, a clue to how Chicago’s economy is shaped over time?"

business_time_series = html.Div(
                            children=[
                                    html.Div(
                                        children = [
                                            html.H3("Like the winds that sweep through the city, businesses rise and fade",
                                                    style={
                                                        'text-align': 'left',
                                                        'color': '#800000',
                                                        'font-size': '30px',
                                                        'font-family': 'Arial, sans-serif',
                                                        'font-weight': 'bold',
                                                        'max-width': '800px',
                                                        'margin': '20px auto',
                                                        'margin-top': '200px',
                                                        }
                                                    ),

                                            html.P(text_gis,
                                                    style={
                                                        'text-align': 'left',
                                                        'max-width': '800px',
                                                        'margin': '20px auto',
                                                        'font-size': '18px',
                                                        'font-family': 'Arial, sans-serif',
                                                        'color': 'black',
                                                        'margin': '20px auto',
                                                        'margin-bottom': '400px'
                                                        }
                                                    )
                                            ],
                                            style = {'padding': '20px'}
                                            ),

                                    html.Div(html.P("put GIS here"),
                                        style={'width': '60%', 'display': 'inline-block', 'padding': '20px'}
                                    )
                                ],
                            
                            style = style_section_split
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

# Callback to update Plot 1 based on selected category
@app.callback(
    [Output('scatter-left', 'figure')],
    [Input('category-dropdown', 'value')]
)

def update_plots(selected_category):
    # Filter data based on selected category
    filtered_df = df[df['category'] == selected_category]
    
    # Generate all the scatter plots (1-6)
    fig1 = create_scatter_plot(filtered_df, 'Scatter Plot 1', 'X Axis 1', 'Y Axis 1')
    
    # Return all six figures for the scatter plots
    return fig1 


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
