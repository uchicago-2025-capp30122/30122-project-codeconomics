from dash import html

intro_layout = html.Div(
                    children=[
                        html.Div(
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
                                    'margin-top': '260px',
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
                                   'width': '70%',
                           'padding': '0',
                           'margin': '0',
                           'background-color':'#800000'}
                        ),

                        html.Img(
                            src = 'https://wallpapercat.com/w/full/d/9/4/1400432-1920x1200-desktop-hd-black-and-white-chicago-skyline-background-photo.jpg',
                            width= '500px',
                            style={
                                'object-fit': 'cover',  # Ensures the image fills the area without distortion
                                'object-position': 'center',  # Centers the cropped image
                                'padding': '0',
                                'margin': '0'
                            }                            
                        )                     
                    ],
                    style = {'height': '100vh', 
                        'padding': '0',
                        'margin':'0',
                        'display': 'flex', 
                        'justify-content': 'space-around'
                                }
                )