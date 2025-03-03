import plotly.express as px
import geopandas as gpd
import json

def create_scatter_plot(df, x, y, x_axis_title, y_axis_title):
    fig = px.scatter(df, x, y,
                     labels={x: x_axis_title, y: y_axis_title},
                     template='plotly_white', trendline="ols")  # Simple white theme
    fig.update_traces(marker=dict(color='#800000'))
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        height=300,  # Set fixed height for each plot
        font=dict(family='Arial, sans-serif', size=14),  # Clean font
    )
    return fig

def create_choropleth(gdf, var, title):
    """
    Create a choropleth map using Plotly Express.
    
    Parameters:
        df (pd.DataFrame): A DataFrame with a 'polygon' column (shapely MultiPolygon) and a column for coloring.
        color_column (str): The column name used for color scaling (default: 'med_income').
    
    Returns:
        fig (plotly.graph_objects.Figure): A choropleth map figure.
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
        hover_name="zip_code",
        hover_data={var:True, 'index': False},  # Display on hover
        mapbox_style="carto-positron",  # Map style
        center={"lat": gdf.geometry.centroid.y.mean()-0.02, "lon": gdf.geometry.centroid.x.mean()},  # Center map
        zoom=9.5,  # Adjust zoom level
        opacity=0.9,  # Adjust opacity
        color_continuous_scale= ["#D9D9D9", "#800000"],
        title=title
    )

    return fig