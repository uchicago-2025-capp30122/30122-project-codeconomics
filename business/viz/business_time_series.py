import plotly.express as px
import pandas as pd
from dash import dcc, html
import plotly.express as px
import pandas as pd
import pathlib

style_section_split = {'height': '100vh',
                        'padding': '5px', 
                        'display': 'flex', 
                        'justify-content': 'space-around'
                    }


# Set time frame for the Viz
min_month = pd.Period("2022-01", freq="M") # Start from Jan 2022
max_month = pd.Period("2024-12", freq="M")  # Ends at Dec 2024
month_range = pd.period_range(min_month, max_month, freq="M") # Get months in between
# Marks: Only at the first and last month
marks = {
    0: min_month.strftime("%Y-%m"),  # First month
    len(month_range) - 1: max_month.strftime("%Y-%m"),  # Last month
}

# Set Path
path_business = pathlib.Path(__file__).parent.parent 

# Load and Wrangle Data
df_time_series = pd.read_csv(path_business / "data/licenses_duration.csv", parse_dates=["initial_date", "final_date"])
df_time_series = df_time_series[(df_time_series['initial_date'].dt.year == 2022)] # Get those started in 2022
df_time_series["operate"] = df_time_series["final_date"].dt.to_period("M").apply( # Get "operate" indicators if they still open in certain date!
    lambda x: "Running" if x >= min_month else "Stopped")
df_time_series = df_time_series.sort_values("operate")  # Sort to ensure consistency in order of points appearing in maps!

def create_maps(df, month):
    # Create the map
    fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        color="operate",
        hover_name="doing_business_as_name",
        hover_data={"license_description": True, "latitude": False, "longitude": False, "operate": False},
        zoom=10,
        mapbox_style="carto-positron",
        color_discrete_map={"Running": "#D9D9D9", "Stopped": "#800000"}
    )

    # Update the layout
    fig.update_layout(title=f"Business Licenses started in 2022 on {month.strftime('%Y-%m')}")

    return fig

# Load Narrative!
with open(path_business / 'viz/text_gis_1.txt', 'r') as text_1:
    text_gis_1 = text_1.read()
with open(path_business / 'viz/text_gis_2.txt', 'r') as text_2:
    text_gis_2 = text_2.read()
with open(path_business / 'viz/text_gis_3.txt', 'r') as text_3:
    text_gis_3 = text_3.read()


business_time_series = html.Div(
                            children=[
                                    html.Div(
                                        children=[                                            
                                            # Graph
                                            dcc.Graph(
                                                id="business-map",
                                                figure=create_maps(df_time_series,month_range[0]),
                                                style={"width": "100%", "height": "80vh", "display": "flex", "flex-direction": "column",
                                                       "margin-top": "50px"}
                                            ),

                                            # Month Slider (cleaner)
                                            dcc.Slider(
                                                id="month-slider",
                                                min=0,
                                                max=len(month_range) - 1,
                                                value=0,
                                                marks=marks,  # Only show quarterly marks
                                                step=1,
                                                updatemode='drag',
                                                tooltip={"placement": "bottom", "always_visible": True}
                                            ),

                                        ],
                                        style={"width": "80%", "height": "100vh"}
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
                                                        'margin-top': '200px',
                                                        }
                                                    ),

                                            html.P(children = [
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
                                                    'margin-bottom': '400px'
                                                    }
                                                )
                                            ],
                                            style = {'padding': '20px'}
                                            )

                                ],
                            
                            style = style_section_split
                        )
