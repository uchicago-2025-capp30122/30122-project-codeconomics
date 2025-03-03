from dash import dcc, html
from business.analyze.business_outlook import get_macro_table
from business.viz.plots import create_scatter_plot
from business.viz.style import *

# # Load Data Macro
df_macro = get_macro_table()
df_macro = df_macro[df_macro['crime_rate'] < 1000] # Removing Outlier

scatters = html.Div(
                    children=[

                        html.Div(
                            children=[
                                html.H3("Business Activity, Income, and Crime: Unraveling the Connections",
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
                                html.P("Can you spot some particular pattern between these variables?",
                                       style = {
                                                'text-align': 'left',
                                                'max-width': '800px',
                                                'margin': '20px auto',
                                        })
                                
                                
                            ]

                        ),
                        
                        html.Div(
                            children=[
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_macro, 'med_income', 'new_rate',
                                                                   x_axis_title='Median Income', y_axis_title='New Business (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_macro, 'crime_rate', 'new_rate',
                                                                   x_axis_title='Crime Rate', y_axis_title='New Business (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_macro, 'theft_rate', 'new_rate',
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
                                        figure=create_scatter_plot(df_macro,'med_income', 'closed_rate',
                                                                   x_axis_title='Median Income', y_axis_title='Turnover (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_macro,'crime_rate', 'closed_rate',
                                                                   x_axis_title='Crime Rate', y_axis_title='Turnover (%Pop)')
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=create_scatter_plot(df_macro,'theft_rate', 'closed_rate',
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