import plotly.express as px
import pandas as pd
from dash import dcc, html
import pathlib
from .style import style_section_split
from ..plots import create_maps

# Set Path
path_business = pathlib.Path(__file__).parent.parent.parent

# Set time frame for the Viz
min_month = pd.Period("2022-01", freq="M") # Start from Jan 2022
max_month = pd.Period("2024-12", freq="M")  # Ends at Dec 2024
month_range = pd.period_range(min_month, max_month, freq="M") # Get range

# Marks for Slider Bar: Only at the first and last month
marks = {
    0: min_month.strftime("%Y-%m"),  # First month
    len(month_range) - 1: max_month.strftime("%Y-%m"),  # Last month
}

# Load Data
df_time_series = pd.read_csv(path_business / "data/licenses_duration.csv",\
                              parse_dates=["initial_date", "final_date"])
# Get those started in 2022
df_time_series = df_time_series[(df_time_series['initial_date'].\
                                 dt.year == 2022)]
# Get "operate" indicators if they still open in certain date!
df_time_series["operate"] = df_time_series["final_date"].dt.to_period("M")\
    .apply(lambda x: "Running" if x >= min_month else "Stopped")
# Sort to ensure consistency in order of points appearing in maps!
df_time_series = df_time_series.sort_values("operate")


# Load Narrative!
with open(path_business / 'viz/dash_section/text_gis_1.txt', 'r') as text_1:
    text_gis_1 = text_1.read()
with open(path_business / 'viz/dash_section/text_gis_2.txt', 'r') as text_2:
    text_gis_2 = text_2.read()
with open(path_business / 'viz/dash_section/text_gis_3.txt', 'r') as text_3:
    text_gis_3 = text_3.read()

# Make a Div Object
business_time_series = html.Div(
                            children=[
                                    html.Div(
                                        children=[
                                            # Graph
                                            dcc.Graph(
                                                id="business-map",
                                                figure=create_maps(df_time_series,month_range[0]),
                                                style={"width": "100%",
                                                       "height": "80vh",
                                                       "display": "flex",
                                                       "flex-direction": "column",                                                       
                                                       "margin-top": "50px"}
                                            ),

                                            # Month Slider
                                            dcc.Slider(
                                                id="month-slider",
                                                min=0,
                                                max=len(month_range) - 1,
                                                value=0,
                                                marks=marks,
                                                step=1,
                                                updatemode='drag',
                                                tooltip={"placement": "bottom",
                                                          "always_visible": True}
                                            ),

                                        ],
                                        style={"width": "80%",
                                               "height": "100vh"}
                                    ),


                                    html.Div(
                                        children = [
                                            html.H3("Like the winds that sweep through the city, businesses rise and fade",
                                                    style={
                                                        'text-align': 'left',
                                                        'color': '#800000',
                                                        'font-size': '25px',
                                                        'font-family': 'Arial, sans-serif',
                                                        'font-style': 'italic',
                                                        'font-weight': 'bold',
                                                        'max-width': '800px',
                                                        'margin': '20px auto',
                                                        'margin-top': '120px',
                                                        }
                                                    ),

                                            html.P(
                                                children = [
                                                    text_gis_1,
                                                    html.Br(),
                                                    text_gis_2,
                                                    html.Br(),
                                                    text_gis_3
                                                ],
                                                style={
                                                    'text-align': 'left',
                                                    'max-width': '800px',
                                                    'margin': '18px auto',
                                                    'font-size': '18px',
                                                    'font-family': 'Arial, sans-serif',
                                                    'color': 'black',
                                                    'margin': '20px auto',
                                                    'margin-bottom': '50px'
                                                }
                                            ),

                                            html.Img(src="https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExM3ZkN3Ywd3Y4MDB4Z2UwcWZ1bTkwamN2bDEwdW54ZjVlODNlOWdncSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/8nM6YNtvjuezzD7DNh/giphy.gif",
                                                     style={'width': '30%',
                                                            'height': 'auto',
                                                            'margin-left':"200px"})
                                        ],
                                        style = {'padding': '20px'}
                                    )
                            ],

                            style = style_section_split
                        )
