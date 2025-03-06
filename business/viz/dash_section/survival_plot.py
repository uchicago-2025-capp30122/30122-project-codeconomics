from ...analyze.survival import business_kmf_plot, business_kmf_plot_crime, business_kmf_plot_income
from dash import html, dcc
from .style import *


survival_plots = html.Div(
                    children=[


                        html.Div(
                            children=[
                                html.H3(children=[
                                    "Survival Analysis of Businesses"
                                ],
                                        style = {
                                                'text-align': 'center',
                                                'color': '#800000',
                                                'font-size': '30px',
                                                'font-family': 'Arial, sans-serif',
                                                'font-weight': 'bold',
                                                'max-width': '1600px',
                                                'margin': '20px auto',
                                                'margin-top': '50px',
                                                'margin-bottom': '20px'
                                        }),
                            ]

                        ),


                        html.Div(
                            children=[
                                html.Div(
                                    dcc.Graph(
                                        figure=business_kmf_plot
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=business_kmf_plot_crime
                                    ),
                                    style = style_scatter
                                ),
                                html.Div(
                                    dcc.Graph(
                                        figure=business_kmf_plot_income
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
