from dash import html
from .style import *

image_hilman = "assets/hilman.png"
image_jorge = "assets/jorge.png"

hilman = html.Div(
    children=[
        html.Img(src=image_hilman,
                 style={
            "width": "150px",
            "height": "150px",
            "border-radius": "50%",
            "object-fit": "cover",
            "align":"center"
        }),
        html.H4('Hilman',style=style_text_contributor),
        html.P('MS-CAPP 2024',style=style_text_contributor)
    ]
)

jorge = html.Div(
    children=[
        html.Img(src=image_jorge,
        style={
            "width": "150px",
            "height": "150px",
            "border-radius": "50%",
            "object-fit": "cover"
        }),
        html.H4('Jorge', style=style_text_contributor),
        html.P('MS-CAPP 2024', style=style_text_contributor)
    ]
)

contributors = html.Div(
    children=[
        html.H2('Codeconomics',
                style={
                    'text-align': 'center',
                    'color': 'orange',
                    'font-size': '50px',
                    'font-family': 'Arial, sans-serif',
                    'font-weight': 'bold',
                    'max-width': '800px',
                    'margin': '20px auto',
                    'margin-top': '80px',
                }),
        html.Div(children=[hilman, jorge],
                 style={'display': 'flex',
                        'justify-content': 'space-around',
                        'padding':'0',
                        'margin':'0'})
    ],
    style={'background-color':'#800000',
           'padding':'2',
           'margin-top':'50px'})
