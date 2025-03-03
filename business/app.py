from dash import Dash, html
from dash.dependencies import Input, Output
import pathlib
from business.viz.choropleth import choropleths
from business.viz.scatters import scatters
from business.viz.business_time_series import df_time_series, month_range, create_maps, business_time_series
from business.viz.style import *

path_data = pathlib.Path(__file__).parent.parent / 'business/data'

# Initialize the Dash app
app = Dash(__name__)


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
