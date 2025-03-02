import plotly.express as px

def create_scatter_plot(df, x, y, x_axis_title, y_axis_title):
    fig = px.scatter(df, x, y,
                     labels={'x': x_axis_title, 'y': y_axis_title},
                     template='plotly_white')  # Simple white theme
    fig.update_traces(marker=dict(color='#800000'))
    fig.update_layout(
        margin=dict(l=20, r=20, t=50, b=20),
        height=300,  # Set fixed height for each plot
        font=dict(family='Arial, sans-serif', size=14),  # Clean font
    )
    return fig

def create_choropleth(df):
    # Create the choropleth map using Plotly
    fig = px.choropleth(
        df,
        geojson=geojson_data,
        locations='zip_code',
        color='median_income',
        hover_name='zip_code',
        color_continuous_scale="Viridis",
        labels={'median_income': 'Median Income'},
    )

    fig.update_geos(fitbounds="locations")
    fig.update_layout(title="Choropleth Map: Median Income by Zip Code")

    return fig