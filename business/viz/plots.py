import plotly.express as px
import geopandas as gpd
import json

def create_scatter_plot(df, x, y, x_axis_title, y_axis_title):
    """
    Create a scatter plot using px.scatter function with further
    adjustment to make the scatter looks in sync

    Arg:
        (Pandas DF) df: the dataframe consisting 2 variables to be plotted
        (str) x: the column of df to be the x axis
        (str) y: the column of df to be the y axis
        (str) x_axis_title: title of x axis
        (str) y_axis_title: title of y axis

    Return:
        (plotly.graph_objects.Figure): the scatter plot (plotly graph object)
    """
    # Make the scatter plot
    # Use OLS function for the trendline
    fig = px.scatter(df, x, y,
                     labels={x: x_axis_title, y: y_axis_title},
                     template='plotly_white', trendline="ols")
    # Recolor the dots to be Maroon
    fig.update_traces(marker=dict(color='#800000'))
    # Adjust margin, size, and font!
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        height=300,
        font=dict(family='Arial, sans-serif', size=14),
    )
    return fig

def create_choropleth(gdf, var, title):
    """
    Create a choropleth map using Plotly Express.

    Args:
        (Pandas df) df: A DataFrame with a 'polygon' column
            (shapely MultiPolygon) and a column for coloring.
        (str) var: The column name used for color scaling
        (str) title: the title of the choropleth

    Returns:
        (plotly.graph_objects.Figure): A choropleth map figure.
    """

    # Convert to GeoJSON format
    geojson_data = json.loads(gdf.to_json())

    # Assign unique IDs for mapping
    gdf["id"] = gdf.index

    # Create Choropleth Map
    fig = px.choropleth_mapbox(
        gdf,
        geojson=geojson_data,
        locations=gdf.index,  # Must match the "id" in geojson
        color=var,  # Column for color scaling
        hover_name="zip_code", # Variables to appear on the cursor plot
        hover_data={var:True},  # Display on hover
        mapbox_style="carto-positron",  # Map style
        center={"lat": gdf.geometry.centroid.y.mean()-0.02,
                 "lon": gdf.geometry.centroid.x.mean()},  # Center map
        zoom=9.5,  # Adjust zoom level
        opacity=0.9,  # Adjust opacity
        color_continuous_scale= ["#D9D9D9", "#800000"],
        title=title
    )

    return fig


def create_maps(df, month):
    """
    Create a visualization of the spatial distribution of business as Points 
    object at certain time

    Args:
    (Pandas df) df: a dataframe contains the individual business data as rows
    and include their initial and end date of license, also Point field as
    in the columns
    (Pd.Period) month: month selected

    Returns:
        (plotly.graph_objects.Figure): A GIS map figure

    """
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