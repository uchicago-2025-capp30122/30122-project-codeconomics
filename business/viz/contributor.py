from dash import html
from .style import *

image_hilman = "https://www.nbc.com/sites/nbcblog/files/2022/07/the-office-how-to-watch.jpg"
image_jorge = "https://www.nbc.com/sites/nbcblog/files/2022/07/the-office-how-to-watch.jpg"

style_text = {'text-align': 'left',
                'color': 'orange',
                'font-size': '25px',
                'font-family': 'Arial, sans-serif',
                'max-width': '800px',
                'margin': '20px auto'
            }

hilman = html.Div(
    children=[
        html.Img(src=image_hilman,
                 style={
            "width": "150px",
            "height": "150px",
            "border-radius": "50%", 
            "object-fit": "cover" 
        }),
        html.H4('Hilman',style=style_text),
        html.P('MS-CAPP 2024',style=style_text)
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
        html.H4('Jorge', style=style_text),
        html.P('MS-CAPP 2024', style=style_text)
    ]
)

contributors = html.Div(
    children=[
        html.H2('Contributors',
                style={
                    'text-align': 'center',
                    'color': '#D9D9D9',
                    'font-size': '50px',
                    'font-family': 'Arial, sans-serif',
                    'font-weight': 'bold',
                    'max-width': '800px',
                    'margin': '20px auto',
                    'margin-top': '50px',
                }),
        html.Div(children=[hilman, jorge],
                 style={'display': 'flex', 
                        'justify-content': 'space-around'})
    ],
    style={'background-color':'#800000',
           'padding':'0',
           'margin':'0'})