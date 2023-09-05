import folium
import contextily as ctx
import plotly.express as px
import pandas as pd
import numpy as np
import geopandas as gpd
from src.dashboard.utils import read_logos
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from IPython.display import display


def show_images_on_dashboard(st, logos_path):
    """Read logos and put it in the dashboard"""
    STCimage, UNICEFimage, DSAimage, _ = read_logos(logos_path)
    st.sidebar.image(STCimage, width=300)
    st.sidebar.image(UNICEFimage, width=300)
    st.sidebar.image(DSAimage, width=150)
    return st


def get_center(df):
    """
    Calculates the geographical center of a GeoDataFrame based on the bounding coordinates.

    Parameters:
    -----------
    df : geopandas.GeoDataFrame
        A GeoDataFrame containing a 'geometry' column with geographical shapes.

    Returns:
    --------
    list
        A list with two elements, the longitude and latitude of the geographical center.
    """
    bounds = df.bounds
    center = [
        (bounds.minx.mean() + bounds.maxx.mean()) / 2,
        (bounds.miny.mean() + bounds.maxy.mean()) / 2,
    ]
    return center


def generate_choropleth(
    combined_df: gpd.GeoDataFrame,
    admin: str,
    column: str,
    legend_name: str,
    fill_color: str = "YlOrRd",
    zoom_start: int = 5,
    **kwargs,
):
    """
    Generates a Folium map with a choropleth layer.

    Parameters:
    -----------
    combined_df : gpd.GeoDataFrame
        The data to use for the map. It should include a 'geometry' column and p.
    admin : str
        The name of the column in combined_df to use for the choropleth. This column
        should contain unique identifiers for the regions in the map.
    column: str
        The name of the column in combined_df to use for the choropleth.
    legend_name: str
        The legend title of the map.
    zoom_start: int, optional
        zoom level of the map
    fill_color : str, optional
        Color palette for the choropleth. Default is "YlOrRd".
        Please change this if you want to plot for something not related to temperature.
        For precipitation it might be good to have green or blue like figure.

    Returns:
    --------
    folium.Map
        A Folium Map object that can be displayed.
    """
    if admin not in combined_df.columns or column not in combined_df.columns:
        raise ValueError(
            f"Required columns ({admin} or {column}) are missing from the dataframe."
        )
    center = get_center(combined_df)
    # Convert the GeoDataFrame to GeoJSON
    geojson_data = combined_df.to_json()

    # Create a Folium map
    m = folium.Map(location=center, zoom_start=zoom_start)

    kwargs.update(
        {
            "geo_data": geojson_data,
            "data": combined_df,
            "columns": [admin, column],
            "key_on": f"feature.properties.{admin}",
            "fill_color": fill_color,
            "nan_fill_color": "white",
            "fill_opacity": 0.7,
            "line_opacity": 0.2,
            "legend_name": legend_name,
            "highlight": True,
            "line_color": "black",
        }
    )

    # Create a choropleth layer
    folium.Choropleth(**kwargs).add_to(m)

    return m


def generate_bivariate_map(
    combined_df_1: gpd.GeoDataFrame,
    combined_df_2: gpd.GeoDataFrame,
    admin: str,
    column_1: str,
    column_2: str,
    legend_1: str,
    legend_2: str,
    zoom_start: int = 5,
    **kwargs,
):
    """
    Generates a Folium map with a choropleth layer.

    Parameters:
    -----------
    combined_df_1 : gpd.GeoDataFrame
        The data to use for the map. It should include a 'geometry' column and p. Also should include column 1.
    combined_df_2 : gpd.GeoDataFrame
        The data to use for the map. It should include a 'geometry' column and p. Also should include column 2.
    admin : str
        The name of the column in combined_df to use for the choropleth. This column
        should contain unique identifiers for the regions in the map.
    column_1: str
        Column 1 (or variable 1) from combined_df_1 to consider for the bivariate map
    column_2: str
        Column 2 (or variable 2) from combined_df_2 to consider for the bivariate map
    legend_1: str
        The legend title for combined_df_1 to consider for the bivariate map
    legend_2: str
        The legend title for combined_df_2 to consider for the bivariate map
    zoom_start: int, optional
        zoom level of the map

    Returns:
    --------
    folium.Map
        A Folium Map object that can be displayed.
    """
    center = get_center(combined_df_1)
    # Convert the GeoDataFrame to GeoJSON
    geojson_data = combined_df_1.to_json()

    # Create a Folium map
    m = folium.Map(location=center, zoom_start=zoom_start)

    # Create a choropleth layer
    folium.Choropleth(
        geo_data=geojson_data,
        data=combined_df_1,
        columns=[admin, column_1],
        key_on=f"feature.properties.{admin}",
        fill_color="Greens",
        nan_fill_color="white",
        fill_opacity=0.7,
        line_opacity=0.2,
        highlight=True,
        line_color="black",
        bins=3,
        legend_name=legend_1
    ).add_to(m)

    folium.Choropleth(
        geo_data=geojson_data,
        data=combined_df_2,
        columns=[admin, column_2],
        key_on=f"feature.properties.{admin}",
        fill_color="Purples",
        nan_fill_color="white",
        fill_opacity=0.7,
        line_opacity=0.2,
        highlight=True,
        line_color="black",
        bins=3,
        legend_name=legend_2
    ).add_to(m)

    # popup = folium.Popup(iframe, max_width=400)
    # marker = folium.Marker(location=center, popup=popup)
    # marker.add_to(m)

    folium.LayerControl().add_to(m)
    return m


def generate_interactive_time_series(df, weather_data_name):
    fig = px.line(df, x="year", y=weather_data_name, title="Time Series of " + weather_data_name)

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        ),
    )
    # fig.show()
    return fig


def plot_poverty_index(
    map_nigeria: gpd.GeoDataFrame, wave_panel_df: gpd.GeoDataFrame, column: str
):
    """
    Plot the poverty index for households on a Nigeria map.

    Parameters:
    - map_nigeria: GeoDataFrame
        A GeoDataFrame representing the map of Nigeria.

    - wave_panel_df: GeoDataFrame
        A GeoDataFrame containing the household points, which has a column that denotes the poverty indicator of each household.
    column:
        Poverty indicator column to visualize
    Returns:
    None. This function will plot the map.
    """

    fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))

    # Plot the Nigeria map
    map_nigeria.to_crs(
        crs="EPSG:3857",  # Use EPSG:3857 for contextily basemaps
    ).plot(ax=ax1, linewidth=1, color="green", alpha=0.5, zorder=2)

    # Plot the household points with color according to the 'mean' column
    wave_panel_df.to_crs(
        crs="EPSG:3857",  # Use EPSG:3857 for contextily basemaps
    ).plot(
        ax=ax1,
        markersize=5,
        column=column,
        cmap="Reds",
        legend=True,
        zorder=3,
    )

    # Add a basemap
    ctx.add_basemap(ax1, source=ctx.providers.Stamen.TonerLite)

    ax1.set_title("")
    return fig
