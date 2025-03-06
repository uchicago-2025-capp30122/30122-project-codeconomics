from dash import Dash, html
from dash.dependencies import Input, Output
import pathlib
from .viz.dash_section.intro import intro_layout
from .viz.dash_section.choropleth import choropleths
from .viz.dash_section.scatters import scatters
from .viz.dash_section.business_time_series import df_time_series, month_range, create_maps, business_time_series
from .viz.dash_section.survival_plot import survival_plots
from .viz.dash_section.contributor import contributors

path_data = pathlib.Path(__file__).parent.parent / 'business/data'

# Initialize the Dash app
app = Dash(__name__)

app.layout = html.Div(
    children=[
        intro_layout,
        business_time_series,
        survival_plots,
        choropleths,
        scatters,
        contributors
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
