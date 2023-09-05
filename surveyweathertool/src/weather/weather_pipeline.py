from typing import Any, Dict, List, Optional, Tuple
import pandas as pd
import numpy as np
import geopandas as gpd
import contextily as ctx
from scipy.stats import gamma, norm
import matplotlib.pyplot as plt
import xarray
import rioxarray
from pandas.api.types import is_datetime64_any_dtype
from datetime import datetime
from src.survey.helper import dataframe_reader
from src.weather.constants import GEO_COLUMNS, PROCESSED_INTERPOLATED_DATA_PATH


from .utils import (
    compute_severity_ranking,
    compute_years_daily_averaging_threshold_per_grid,
    initialize_features_columns,
    check_file_existence,
    extract_timescales,
    thresholds_saver_loader,
    batching
)


def aggr_monthly(df, column_aggr=""):
    """
    Aggregates the weather data in the DataFrame on a monthly basis.

    Parameters:
    df (pandas.DataFrame): DataFrame containing weather data with a DateTime column.
    column_aggr: Column to aggregate, for example, temp or precip

    Returns:
    df_monthly (pandas.DataFrame): New DataFrame containing the mean, max, and min weather grouped by month,
    year, latitude, and longitude.
    """
    if column_aggr not in df.columns:
        raise ValueError(f"The {column_aggr} is not part of the columns")

    if "date" not in df.columns:
        raise ValueError("date column is not part of the columns")

    if not is_datetime64_any_dtype(df["date"]):
        if df["date"].isnull().any():
            raise ValueError("There are null values in the 'date' column.")
        df["date"] = pd.to_datetime(df["date"])

    # Group by month, latitude, longitude, and year, then calculate the mean, max and min column_aggr
    df_monthly = (
        df.groupby(["year", "month", "lon", "lat"])[column_aggr]
        .agg(["mean", "max", "min"])
        .reset_index()
    )

    return df_monthly


def aggr_yearly(df, column_aggr=""):
    """
    Aggregates the weather data in the DataFrame on a monthly basis.

    Parameters:
    df (pandas.DataFrame): DataFrame containing weather data with a DateTime index.
    column_aggr: Column to aggregate, for example, temp or precip

    Returns:
    df_monthly (pandas.DataFrame): New DataFrame containing the mean, max, and min weather grouped by month,
    year, latitude, and longitude.
    """
    if column_aggr not in df.columns:
        raise ValueError(f"The {column_aggr} is not part of the columns")

    # Group by month, latitude, longitude, and year, then calculate the mean, max and min column_aggr
    df_yearly = (
        df.groupby(["year", "lon", "lat"])[column_aggr].agg(["mean", "max", "min"]).reset_index()
    )

    return df_yearly


def convert_point_crs(df, target_epsg, source_epsg=4326):
    """
    Convert a DataFrame with 'lon' and 'lat' columns to a GeoDataFrame with specified geometry.

    Parameters:
    - df (pd.DataFrame): Input DataFrame with 'lon' and 'lat' columns.
    - target_epsg (str): Desired EPSG code for output GeoDataFrame.
    - source_epsg (str, optional): The EPSG code of the input DataFrame's 'lon' and 'lat' columns.
                                   Default is "EPSG:4326" (WGS84 latitude-longitude).

    Returns:
    - gpd.GeoDataFrame: GeoDataFrame with geometry set and reprojected to the desired EPSG.
    """
    df_pts = gpd.points_from_xy(x=df["lon"], y=df["lat"], crs=f"EPSG:{source_epsg}")
    df_pts = gpd.GeoDataFrame(df, geometry=df_pts).to_crs(epsg=target_epsg)

    # Update the 'lon' and 'lat' columns based on the reprojected geometry
    df_pts["lon"] = df_pts.geometry.x
    df_pts["lat"] = df_pts.geometry.y
    return df_pts


def convert_map_crs(geo_df: pd.DataFrame, epsg: int) -> gpd.GeoDataFrame:
    """
    Convert the CRS of a DataFrame or GeoDataFrame to a specified EPSG code.

    Parameters:
    - geo_df (pd.DataFrame): The input DataFrame or GeoDataFrame.
    - epsg (int): The EPSG code for the desired Coordinate Reference System.

    Returns:
    - gpd.GeoDataFrame: The GeoDataFrame with the new CRS.
    """
    if not isinstance(geo_df, gpd.GeoDataFrame):
        geo_df = gpd.GeoDataFrame(geo_df, crs=epsg, geometry="geometry")
    else:
        geo_df = geo_df.to_crs(epsg=epsg)
    return geo_df


def aggr_seasonal(df):
    """
    Aggregate data by season, latitude, longitude, and year, and calculates the mean, max, and min values.

    This function adds a new column 'season' to the dataframe, which categorizes each month into one of the four seasons:
    Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November), Winter (December, January, February).
    It then groups the data by season, latitude, longitude, and year and calculates the mean values for 'mean', 'max', and 'min' columns.

    Parameters:
    df (pandas.DataFrame): A pandas DataFrame that contains columns 'month', 'lat', 'lon', 'year', 'mean', 'max', and 'min'.

    Returns:
    df_seasonal (pandas.DataFrame): A pandas DataFrame with the aggregated data.
    """

    def assign_season(month):
        if month in [3, 4, 5]:
            return "Spring"
        elif month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"
        else:
            return "Winter"

    # Add a new column for season
    df["season"] = df["month"].map(assign_season)

    # Group by season, latitude, longitude, and year, then calculate the mean, max, and min
    df_seasonal = (
        df.groupby(["season", "lat", "lon", "year"])
        .agg({"mean": "mean", "max": "mean", "min": "mean"})
        .reset_index()
    )

    return df_seasonal


def aggr_seosonal_nigeria(df):
    """
    Aggregate data by season, latitude, longitude, and year, and calculates the mean, max, and min values.
    This function is same as aggr_seasonal but decided Nigeria's two seasons
    """

    def assign_season(month):
        if month in [i for i in range(4, 10)]:
            return "Wet"
        else:
            return "Dry"

    expected_columns = ["min", "max", "mean", "month"]
    if not np.all(np.isin(expected_columns, df.columns.tolist())):
        raise ValueError(f"{expected_columns} is not part of the columns")

    # Add a new column for season
    df["season"] = df["month"].map(assign_season)

    # Group by season, latitude, longitude, and year, then calculate the mean, max, and min
    df_seasonal = (
        df.groupby(["season", "lat", "lon", "year"])
        .agg({"mean": "mean", "max": "mean", "min": "mean"})
        .reset_index()
    )

    return df_seasonal


def combine(
    map_df, other_df, col_dissolve, group_cols=None, agg_dict={}, method="intersects"
):
    """
    Function to combine two GeoDataFrames based on a spatial join operation and group by operations.

    Parameters
    ----------
    map_df : geopandas.GeoDataFrame
        The GeoDataFrame with the geometry column to be used for the spatial join.

    other_df : geopandas.GeoDataFrame
        The GeoDataFrame with data to be joined with map_df.

    col_dissolve : str
        The column name in map_df used to dissolve the geometry into unique polygons.

    group_cols : list
        List of columns to group by in addition to col_dissolve and geometry.

    agg_dict : dict
        Dictionary of aggregation functions for specified columns.

    method : str, optional
        The method to be used for the spatial join operation. It could be "intersects", "within", "contains", etc.
        Default is "intersects".

    Returns
    -------
    admin_db : geopandas.GeoDataFrame
        The GeoDataFrame resulting from the spatial join and group by operations.

    """
    dissolved_df = map_df.dissolve(col_dissolve).reset_index()
    admin_db = gpd.sjoin(dissolved_df, other_df, predicate=method)
    if not bool(agg_dict):
        raise ValueError(
            "agg_dict is empty, provide dictionary with column and aggregation mechanism"
        )
    # Group by and aggregate. Using 'first' for the geometry assumes that the geometry for each group is identical
    agg_dict["geometry"] = "first"
    admin_db = admin_db.groupby([col_dissolve] + group_cols).agg(agg_dict).reset_index()
    return admin_db


def create_df_final(
    nigeria_shape_df,
    weather_df,
    col_dissolve,
    target_epsg,
    weather_data_name,
    agg_dict,
    level,
):
    """
    This function creates a final dataframe by combining weather and shapefile data

    Parameters:
    -----------
    nigeria_shape_df: geopandas.GeoDataFrame
        Nigeria map with admin columns
    weather_df : geopandas.GeoDataFrame
        Weather data, geopandas.GeoDataFrame with columns ['precipitation', 'temperature', 'spi', 'heatwaves', 'heavyrain']
    col_dissolve : str
        Column name on which to dissolve boundaries when merging the shapefile and weather data.
    target_epsg: target epsg to use
    weather_data_name:
        This is weather name, wether precipitation or temperature.
        Currenly not in use properly but will be used better when different positions are created for each weather event in the dashboard
    agg_dict: dict
        Dictionary to with column names and the aggregation method to perform
    level: str
        "month" or "season" level to group on

    Returns:
    --------
    pandas.DataFrame
        A dataframe containing the merged shapefile and weather data.

    """

    if level == "month":
        aggr_weather_df = aggr_monthly(
            df=weather_df.copy(), column_aggr=weather_data_name
        )
        group_cols = ["year", "month"]
    elif level == "season":
        # aggregate seasonally
        aggr_weather_df = aggr_monthly(
            df=weather_df.copy(), column_aggr=weather_data_name
        )
        aggr_weather_df = aggr_seosonal_nigeria(df=aggr_weather_df.copy())
        group_cols = ["year", "season"]
    elif level == "year":
        # aggregate yearly
        aggr_weather_df = aggr_yearly(
            df=weather_df.copy(), column_aggr=weather_data_name
        )
        group_cols = ["year"]
    
    else:
        aggr_weather_df = weather_df
        group_cols = []
    # convert the dataframe to geopandas with geometry
    weather_df_pts = convert_point_crs(df=aggr_weather_df, target_epsg=target_epsg)
    df_final = combine(
        map_df=nigeria_shape_df,
        other_df=weather_df_pts,
        col_dissolve=col_dissolve,
        agg_dict=agg_dict,
        group_cols=group_cols,
    )
    df_final = convert_map_crs(df_final, epsg=target_epsg)
    return df_final


def extreme_thresholding_delta(
    row: Dict[str, Any],
    event: str,
    geo_columns: List[str],
    threshold_values: Dict[str, List[float]],
    delta_param: Optional[int],
) -> Tuple[float, bool]:
    """
    Calculate the delta between an event's value and its threshold value, and check if it exceeds a delta parameter.

    Parameters:
        row (Dict[str, Any]): A dictionary representing a row of data.
        event (str): The name of the event.
        geo_columns (List[str]): List of column names containing longitude and latitude.
        threshold_values (Dict[str, List[float]]): A dictionary of threshold values indexed by unique geo keys.
        delta_param (Optional[int]): The delta parameter value. If not provided, defaults to 0.

    Returns:
        Tuple[float, bool]: A tuple containing the calculated delta and a boolean indicating if the delta exceeds the delta parameter.
    """
    if not delta_param:
        delta_param = 0

    longitude, latitude = geo_columns
    threshold_key = f"{row[longitude]}-{row[latitude]}"

    threshold_value = threshold_values[threshold_key][row["day"] - 1]
    delta = row[event] - threshold_value
    
    if delta < 0:
        return (0, False)
    return (delta, delta > delta_param)


def create_extreme_weather_event_delta(
    data: pd.DataFrame,
    event: str,
    geo_columns: List[str],
    daily_thresholds: Dict[str, List[float]],
    delta_param: Optional[int] = None,
) -> None:
    """
    Calculate deltas and identify extreme weather events based on given thresholds.

    Parameters:
        data (pd.DataFrame): DataFrame containing weather data.
        event (str): The name of the event.
        geo_columns (List[str]): List of column names containing longitude and latitude.
        daily_thresholds (Dict[str, List[float]]): A dictionary of daily threshold values indexed by unique geo keys.
        delta_param (Optional[int]): The delta parameter value. If not provided, defaults to None.

    Returns:
        None: The function modifies the 'data' DataFrame by adding 'delta' and 'extreme' columns.
    """
    
    data[["delta", "extreme"]] = data.apply(
        extreme_thresholding_delta,
        args=(event, geo_columns, daily_thresholds, delta_param),
        axis=1,
        result_type="expand",
    )
    


def heatwave_heavy_rainfall_indicators(
    data: pd.DataFrame,
    event: str,
    geo_columns: List[str],
    rolling_window: int = 3,
    delta_param: int = 5,
    days_param: int = 3,
    batch_size: int = 3,
):
    """
    Compute heatwave or heavy rainfall indicators for extreme weather event definition.

    Parameters:
        data (pd.DataFrame): The DataFrame containing weather data with 'date', 'event', and specified geo_columns.
        event (str): The weather event name (e.g., 'temperature', 'rainfall').
        geo_columns (List[str]): List of columns representing geographic information.
        on_survey (bool, optional): Flag indicating whether the function is being run on a survey. Default is False.
        rolling_window (int, optional): Rolling window size for computing daily averaging thresholds. Default is 3.
        delta_param (int, optional): Delta parameter for creating extreme weather event delta. Default is 5.
        days_param (int, optional): Days parameter for creating extreme weather event delta. Default is 3.

    Returns:
        None. Computes and saves the relevant indicators based on the specified parameters.
    """
    geo_columns = GEO_COLUMNS
        
    indicator_filename = "all_temperature_interpolated_indicators" if event.startswith("temp") else "all_precipitation_indicators"
    indicator_path = f"{PROCESSED_INTERPOLATED_DATA_PATH}/{indicator_filename}.pickle"

    if check_file_existence(indicator_path):
        print(
            f"[FINISH] The weather event indicator already exist in {indicator_path}"
        )
        data = dataframe_reader(indicator_path)
        return data

    columns = geo_columns + ["date", event]
    columns_exist = all(col in data.columns for col in columns)

    if not columns_exist:
        print(f"Ensure {columns} is defined in the data")
        return

    print(
        f"[START] {event.title()} Delta, Severity & Ranking Computation for MOC/IPCC Extreme Weather Event Definition"
    )
    
    extract_timescales(data)

    if event.startswith("temp"):
        daily_averaging_thresholds_path = (
            f"{PROCESSED_INTERPOLATED_DATA_PATH}/daily_averaging_{event}_interpolated_thresholds.pkl"
        )
    else:
        daily_averaging_thresholds_path = (
            f"{PROCESSED_INTERPOLATED_DATA_PATH}/daily_averaging_{event}_thresholds.pkl"
        )

    if not check_file_existence(daily_averaging_thresholds_path):
        print(f"{'=' * 3 }> Historical {event} Daily Averaging Thresholds")
        daily_averaging_thresholds = compute_years_daily_averaging_threshold_per_grid(
            data, event, geo_columns, rolling_window
        )
        thresholds_saver_loader(
            daily_averaging_thresholds_path, daily_averaging_thresholds
        )
    else:
        daily_averaging_thresholds = thresholds_saver_loader(
            daily_averaging_thresholds_path, action="load"
        )
    
    def _get_indicator_features(subset_data: pd.DataFrame, event: str, geo_columns: List[str], daily_averaging_thresholds: dict, delta_param: int, days_param: int) -> None:
        """
        Compute indicator features for a subset of data.

        Parameters:
            subset_data (pd.DataFrame): Subset of data to compute indicator features on.
            event (str): Event column to compute features for.
            geo_columns (list of str): Columns representing geographical coordinates.
            daily_averaging_thresholds (dict): Dictionary containing daily averaging thresholds.
            delta_param (int): Delta parameter for thresholding.
            days_param (int): Number of days for parameter computation.
        """
        create_extreme_weather_event_delta(subset_data, event, geo_columns, daily_averaging_thresholds, delta_param)
        initialize_features_columns(subset_data)
        compute_severity_ranking(subset_data, event, days_param)
   
    # Sort the unique years in data and check whether number of years is bigger than batch_size
    unique_years = sorted(data.year.unique())
    batched = len(unique_years) > batch_size
    
    if batched:
        batched_years = batching(unique_years, batch_size)
        batched_data = []

        start_time = datetime.now()
        
        for phase, batch_years in enumerate(batched_years):
            batch_years_data = data[data.year.isin(batch_years)].copy()
            print(f"  {'=' * 3 } Batch {phase + 1} Featurization Computation - {batch_years} | {batch_years_data.shape[0]} points")

            _get_indicator_features(batch_years_data, event, geo_columns, daily_averaging_thresholds, delta_param, days_param)
            batched_data.append(batch_years_data)

        print(datetime.now() - start_time)
        del batch_years_data
        data = pd.concat(batched_data, ignore_index=True)
    else:
        _get_indicator_features(data, event, geo_columns, daily_averaging_thresholds, delta_param, days_param)
    
    print(f"[FINISH]")
    return data


def combine_map_weather(
    nigeria_shape_df,
    weather_df,
    col_dissolve,
    weather_data_name,
    agg_dict,
    level,
    target_epsg,
):
    """
    Combines map data with different types of weather data and returns a unified dataframe.

    Parameters:
    -----------
    nigeria_shape_df: geopandas.GeoDataFrame
        Nigeria map with administrative columns.
    weather_precipitation_df : geopandas.GeoDataFrame
        Weather data containing precipitation.
    weather_temperature_df : geopandas.GeoDataFrame
        Weather data containing temperature.
    weather_spi_df : geopandas.GeoDataFrame
        Weather data containing spi.
    col_dissolve: str
        Column name to dissolve boundaries when merging the shapefile and weather data.
    weather_data_name: str
        Specifies the type of weather data. Options include "temperature", "precipitation", "spi", "heatwave", and "heavyrain".
    agg_dict: dict
        Dictionary with column names and the aggregation method to perform.
    level: str
        Specifies the level to group on. e.g. "month" or "season".
    target_epsg: int
        The target epsg code to use for the geographical transformations.

    Returns:
    --------
    pandas.DataFrame
        A dataframe containing the merged shapefile and specified weather data.
    """
    df_final = create_df_final(
        nigeria_shape_df=nigeria_shape_df,
        weather_df=weather_df,
        col_dissolve=col_dissolve,
        target_epsg=target_epsg,
        weather_data_name=weather_data_name,
        agg_dict=agg_dict,
        level=level,
    )

    return df_final


def calculate_SPI(df, column_rol="precipitation"):
    """
    Calculates the Standardized Precipitation Index (SPI) for given input data.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing precipitation data.
    - column_rol (str, optional): Column in the DataFrame containing precipitation data
                                  that will be used to calculate the rolling mean.
                                  Defaults to 'precipitation'.
    - save (bool, optional): If to save the spi to a csv file. Defaults to False
    - save (str, optional): Path to save the spi file. Defaults to spi_file.csv

    Returns:
    - df (pd.DataFrame): DataFrame with added columns for 3-month rolling mean of precipitation,
                         cumulative probability, and the 3-month SPI.
    """

    # Compute 3-month rolling mean
    df["3_month_precip_mean"] = df[column_rol].rolling(window=90, min_periods=1).mean()
    # Add a small constant to the data
    small_constant = 0.001
    df["3_month_precip_mean"] = df["3_month_precip_mean"] + small_constant

    # Check and print any NaN values
    nan_values = df["3_month_precip_mean"].isna().sum()
    if nan_values > 0:
        print(f"Found {nan_values} NaN values in '3_month_precip_mean'.")

    # Check and print any negative values
    negative_values = (df["3_month_precip_mean"] < 0).sum()
    if negative_values > 0:
        print(f"Found {negative_values} negative values in '3_month_precip_mean'.")

    # Check and print any zero values
    zero_values = (df["3_month_precip_mean"] == 0).sum()
    if zero_values > 0:
        print(f"Found {zero_values} zero values in '3_month_precip_mean'.")

    # Function to calculate cumulative probability for each lat-lon pair
    def calculate_cumulative_prob(data, shape, scale):
        return gamma.cdf(data["3_month_precip_mean"], shape, loc=0, scale=scale)

    df["cumulative_prob"] = pd.Series(dtype="float64")
    unique_points = df[["lat", "lon"]].drop_duplicates().values
    print(f"number of unique_points: {len(unique_points)}")
    for lat, lon in unique_points:
        data = df[(df["lat"] == lat) & (df["lon"] == lon)]

        # Compute gamma parameters
        shape, loc, scale = gamma.fit(data["3_month_precip_mean"], floc=0)

        # Calculate and store the cumulative probability
        df.loc[data.index, "cumulative_prob"] = calculate_cumulative_prob(
            data, shape, scale
        )

    # Convert cumulative probability to Z-scores to obtain the SPI
    df["SPI"] = df["cumulative_prob"].apply(lambda x: norm.ppf(x))
    return df


def xarray_upsample(da, lat_res, lon_res, method):
    """
    Upsample an xarray DataArray based on the provided latitude and longitude resolutions.

    Parameters:
    -----------
    da : xarray.DataArray
        The input DataArray to be upsampled.

    lat_res : float
        The desired latitude resolution for upsampling.

    lon_res : float
        The desired longitude resolution for upsampling.

    method : str
        The interpolation method to be used for upsampling. Supported methods are
        the same as those for xarray's `interp` method (e.g., "linear", "nearest").

    Returns:
    --------
    xarray.DataArray
        The upsampled DataArray with new latitude and longitude resolutions.
    """
    # Create new coordinates for interpolation
    new_lat = np.arange(da["y"].min(), da["y"].max() + lat_res, lat_res)
    new_lon = np.arange(da["x"].min(), da["x"].max() + lon_res, lon_res)

    # Use xarray's interpolate_na method
    upsampled_da = da.interp(y=new_lat, x=new_lon, method=method)

    return upsampled_da


def clip_data(
    df: pd.DataFrame,
    geo_df: gpd.GeoDataFrame,
    epsg: int = 4326,
):
    """
    Processes and clips weather data in the DataFrame to a specified geographical region.

    Parameters:
    ----------
    df : pd.DataFrame
        Input DataFrame with weather data that includes columns: date, lat, lon, and the specified value (e.g., temperature).

    geo_df : gpd.GeoDataFrame
        Geographic DataFrame (e.g., a map of Nigeria) used to clip the weather data.

    epsg : int, optional
        EPSG code to set the Coordinate Reference System (CRS) for the data. Defaults to 4326 (WGS 84).

    Returns:
    -------
    pd.DataFrame
        A DataFrame with the combined, processed, and interpolated weather data, clipped to the specified region (from 'geo_df').
        The DataFrame includes columns: lat, lon, the specified weather value (e.g., temperature), and date.
    """
    if geo_df.crs.to_epsg() != epsg:
        raise ValueError(
            f"The map crs and desired weather crs don't match: {geo_df.crs.to_epsg()} != {epsg}"
        )

    df = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat), crs=f"EPSG:{epsg}")
    clipped_df = gpd.clip(df, geo_df)
    return clipped_df


def interpolate_data(
    df: gpd.GeoDataFrame,
    geo_df: gpd.GeoDataFrame,
    value_col: str,
    lat_res: float = 0.1,
    lon_res: float = 0.1,
    method="linear",
    epsg: int = 4326,
):
    """
    Processes and interpolates weather data for each unique date in the DataFrame,
    and clips the interpolated data to a specified geographical region.

    Parameters:
    ----------
    df : gpd.GeoDataFrame
        Input DataFrame with weather data that includes columns: date, lat, lon, and the specified value (e.g., temperature).

    geo_df : gpd.GeoDataFrame
        Geographic DataFrame (e.g., a map of Nigeria) used to clip the interpolated weather data.

    value_col : str
        Column name in 'df' with weather values (e.g., temperature) to be visualized and interpolated.

    lat_res : float, optional
        Latitude resolution for interpolation. Defaults to 0.1.

    lon_res : float, optional
        Longitude resolution for interpolation. Defaults to 0.1.

    method : str, optional
        Interpolation method to use. Can be 'linear', 'nearest', etc. depending on the available methods in the underlying library. Defaults to 'linear'.

    epsg : int, optional
        EPSG code to set the Coordinate Reference System (CRS) for the data. Defaults to 4326 (WGS 84).

    Returns:
    -------
    pd.DataFrame
        A DataFrame with the combined, processed, and interpolated weather data, clipped to the specified region (from 'geo_df').
        The DataFrame includes columns: lat, lon, the specified weather value (e.g., temperature), and date.
    """
    if geo_df.crs.to_epsg() != epsg:
        raise ValueError(
            f"The map crs and desired weather crs don't match: {geo_df.crs.to_epsg()} != {epsg}"
        )

    date = df.loc[0]["date"]
    df["x"] = df.lon
    df["y"] = df.lat
    da = df.set_index(["y", "x"])[value_col].to_xarray()
    da.rio.write_crs(f"EPSG:{epsg}", inplace=True)
    upsampled_da = xarray_upsample(
        da=da, lat_res=lat_res, lon_res=lon_res, method=method
    )
    clipped_upsampled_da = clip_dataarray(da=upsampled_da, geo_df=geo_df)
    df = clipped_upsampled_da.to_dataframe().dropna().reset_index()
    df.rename(columns={"x": "lon", "y": "lat"}, inplace=True)
    df.drop(columns=["spatial_ref"], inplace=True)
    df["date"] = date
    return df


def clip_dataarray(da: xarray.DataArray, geo_df: gpd.GeoDataFrame) -> xarray.DataArray:
    """
    Clip a DataArray based on the shape of a GeoDataFrame.

    Parameters:
    - da (xarray.DataArray): The input DataArray.
    - geo_df (gpd.GeoDataFrame): The GeoDataFrame to use for clipping.

    Returns:
    - xarray.DataArray: The clipped DataArray.
    """
    return da.rio.clip(geo_df.geometry)


def plot_heatmap_grid_on_map(
    df: gpd.GeoDataFrame,
    value_col: str,
    geo_df: gpd.GeoDataFrame,
    cmap: str,
    legend_title: str,
    clip: bool = False,
    epsg: int = 4326,
):
    """
    Plots a heatmap for a given value column on a grid based on the provided GeoDataFrame.
    NB: Use 'Reds' for temperature related plots, and 'Greens' for precipitations related plots

    Parameters:
    ----------
    df : gpd.GeoDataFrame
        The GeoDataFrame containing the data to be plotted.
    value_col : str
        The column name in df which contains the values to be plotted on the heatmap.
    geo_df : gpd.GeoDataFrame
        The GeoDataFrame to use for clipping. Defaults to None.
    clip : bool, optional
        Clips the data to the map. If True geo_df should be provided.
    epsg : int, optional (default=4326)
        The EPSG code representing the coordinate reference system (CRS) of the input data. Default is EPSG:4326 (WGS 84).

    Returns:
    -------
    None
        Displays a heatmap plot.
    """
    df["x"] = df.lon
    df["y"] = df.lat
    da = df.set_index(["y", "x"])[value_col].to_xarray()
    da.rio.write_crs(f"EPSG:{epsg}", inplace=True)

    if clip:
        assert isinstance(geo_df, gpd.GeoDataFrame), "clip requested but geo_df is None"
        assert (
            geo_df.crs.to_epsg() == epsg
        ), f"The map crs and desired weather crs don't match: {geo_df.crs.to_epsg()} != {epsg}"
        da = clip_dataarray(da=da, geo_df=geo_df)

    fig, ax1 = plt.subplots(1, 1, figsize=(8, 6))
    geo_df.plot(
        ax=ax1,
        linewidth=1,
        facecolor="white",
        edgecolor="gray",
        alpha=0.5,
        zorder=1,
        label=legend_title
    )
    da.plot(ax=ax1, zorder=2, alpha=0.7, cmap=cmap)
    ctx.add_basemap(ax1, source=ctx.providers.CartoDB.Positron, zoom=20)
    ax1.set_xlabel("lon")
    ax1.set_ylabel("lat")
    ax1.set_title("")
    plt.axis("off")
    return fig


def interpolate_data_for_all_dates(
    df: gpd.GeoDataFrame,
    geo_df: gpd.GeoDataFrame,
    value_col: str,
    lat_res: float = 0.1,
    lon_res: float = 0.1,
    method: str = "linear",
    epsg: int = 4326,
):
    """
    Interpolates weather data for each unique date in the DataFrame.

    Parameters are the same as in the 'interpolate_data' function.

    Returns:
    -------
    pd.DataFrame
        A DataFrame with interpolated weather data for all dates, clipped to the specified region.
    """
    # List to store dataframes after interpolation for each date
    dfs = []

    # Iterate over each unique date
    for date in df["date"].unique():
        # Filter the dataframe for the specific date
        df_date = df[df["date"] == date].reset_index(drop=True)

        # Interpolate data for the date and append to the list
        interpolated_df = interpolate_data(
            df=df_date.copy(),
            geo_df=geo_df,
            value_col=value_col,
            lat_res=lat_res,
            lon_res=lon_res,
            method=method,
            epsg=epsg,
        )
        dfs.append(interpolated_df)

    # Concatenate all the dataframes in the list
    result_df = pd.concat(dfs, axis=0).reset_index(drop=True)

    return result_df
