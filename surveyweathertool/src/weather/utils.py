from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import geopandas as gpd
import pandas as pd
import xarray as xr
import streamlit as st
import wget
import os
import pickle
from typing import Any, List, Union, Dict, Tuple
from .constants import GEO_COLUMNS
import numpy as np
from pathlib import Path
from itertools import zip_longest
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
import time


# Sourcing the online data using wget
def get_data(baseURL, destination_path, weather, year_start, year_end):
    """
    Download weather data files for a range of years from a given URL.

    Parameters:
    baseURL (str): Base URL of the weather data files.
    destination_path (str): Directory where downloaded files will be stored.
    weather (str): Type of weather data (e.g., "precip", "tmax", "tmin").
    year_start (int): Starting year of the range.
    year_end (int): Ending year of the range.
    """
    print(
        f"Starting to get the data for {weather} from year {year_start} to {year_end} from the URL {baseURL}"
    )

    # Check if destination_path already exists; if not: create it

    print(f"The destination_path is: {destination_path}")
    os.makedirs(destination_path, exist_ok=True)

    for year in range(year_start, year_end + 1):
        print(f"Get data for year {year}")
        dataURL = baseURL + str(year) + ".nc"
        print(type(destination_path))

        file_path = f"{destination_path}/{weather}.{year}.nc"
        print(f"The file_path is: {file_path}")
        print(f"The URL for downloading the data is: {dataURL}")

        wget.download(dataURL, out=file_path)


def ncToCSV(filepath, destination_path, coordinate_limits):
    """
    Convert a NetCDF file to CSV format and filter data based on coordinates.

    Parameters:
    filepath (Path): Path to the input NetCDF file.
    destination_path (Path): Path where the CSV file will be saved.
    coordinate_limits (list): List of latitude and longitude coordinate limits.

    Notes:
    This function assumes that the NetCDF file has a 'time', 'lat', 'lon', and 'precip'/'temp' columns.
    """
    df = xr.open_dataset(filepath).to_dataframe()
    print(filepath)
    df = df.reset_index()
    df = df.set_index("time")

    finalDF = df[
        (df["lat"] >= coordinate_limits[0])
        & (df["lat"] <= coordinate_limits[1])
        & (df["lon"] >= coordinate_limits[2])
        & (df["lon"] <= coordinate_limits[3])
    ]

    finalDF.to_csv(destination_path)
    print(f"Exported to {destination_path}")


def get_correlation_matrix(df, col_index, col_columns, col_values):
    """
    Performs correlation analysis on a given dataframe.

    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe with time series data.
    col_index : str
        Name of the column in df to use as the new dataframe index (time period).
    col_columns : str
        Name of the column in df to use for creating the new dataframe columns (regions).
    col_values : str
        Name of the column in df to use for the data values (mean precipitation).

    Returns:
    --------
    pandas.DataFrame
        A correlation matrix of the data.
    """
    # Pivot the data to create a time series for each region
    df_pivot = df.pivot_table(index=col_index, columns=col_columns, values=col_values)

    # Calculate the correlation matrix
    corr_matrix = df_pivot.corr()

    return corr_matrix


def time_series_clustering(
    df, col_dissolve, time_cols, value_col, eps=2, min_samples=4
):
    """
    Performs time series analysis and clustering on a given dataframe.


    Parameters:
    -----------
    df : pandas.DataFrame
        Input dataframe with time series data.
    col_dissolve : str
        Name of the column in df to use as the new dataframe index.
    time_cols : list of str
        Names of the columns in df to use for creating the time period labels.
    value_col : str
        Name of the column in df to use for the time series values.
    eps : float, optional
        The maximum distance between two samples for them to be considered as in the same neighborhood in DBSCAN. Defaults to 2.
    min_samples : int, optional
        The number of samples in a neighborhood for a point to be considered as a core point in DBSCAN. Defaults to 4.

    Returns:
    --------
    pandas.DataFrame
        A dataframe with the same index as the input dataframe and an additional column 'Cluster' with the DBSCAN cluster labels.
    """
    # Pivot the data to create a time series for each region
    time_series_df = df.pivot_table(
        index=col_dissolve, columns=time_cols, values=value_col
    )

    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(time_series_df)

    # Apply DBSCAN
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    clusters = dbscan.fit_predict(standardized_data)

    # Add the cluster labels to the original dataframe
    time_series_df["Cluster"] = clusters

    # Reset index
    clusters_df = time_series_df.reset_index()

    # Merge clusters back into the original dataframe
    df.sort_index(inplace=True)
    df_final = pd.merge(df, clusters_df, how="left", on=[col_dissolve])
    df_final.columns = df_final.columns.map(
        lambda x: f"{x[0]}_{x[1]}" if isinstance(x, tuple) else x
    )
    df_final.rename(columns={"Cluster_": "Cluster"}, inplace=True)
    return df_final


def compute_dtw(series_1, series_2):
    """
    Compute the Dynamic Time Warping (DTW) distance between two time series.

    Parameters:
    series_1, series_2 : array-like
        Input time series.

    Returns:
    dtw_distance : float
        DTW distance between the input time series.
    """
    arr_1 = series_1.values.reshape(-1, 1)
    arr_2 = series_2.values.reshape(-1, 1)
    dtw_distance, _ = fastdtw(arr_1, arr_2, dist=euclidean)
    return dtw_distance


def create_spi_category(df):
    """
    Create a new feature 'SPI_Category' in the dataframe based on the '3_month_SPI' values.

    Parameters:
    - df (pd.DataFrame): DataFrame with '3_month_SPI' values.

    Returns:
    - df (pd.DataFrame): DataFrame with the added 'SPI_Category' column.
    """

    # Define the bins for SPI values
    bins = [-float("inf"), -2, -1.5, -1, 1, 1.5, 2, float("inf")]

    # Define the labels for the bins
    labels = [
        "Extremely Dry",
        "Moderately Dry",
        "Dry",
        "Neutral",
        "Wet",
        "Moderately Wet",
        "Extremely Wet",
    ]

    # Create a new feature 'SPI_Category' that holds the categories
    df["SPI_Category"] = pd.cut(df["3_month_SPI"], bins=bins, labels=labels)

    return df


@st.cache_data
def read_shape_file(data_path):
    """
    Reads a shapefile and pre-processes it by removing certain columns.

    Parameters:
    -----------
    data_path : str
        The file path to the shapefile.

    Returns:
    --------
    geo_nig : GeoDataFrame
        The pre-processed geopandas dataframe.

    Notes:
    ------
    This function is specifically designed for shapefiles that contain the following columns:
    'admin2AltN', 'admin2Al_1', 'ValidTo', 'date', 'validOn', 'Shape_Leng', 'Shape_Area', 'admin0Name', 'admin0Pcod'.
    These columns will then be removed from the original data.
    # if we need some of the the columns we can further change this function.
    """
    geo_nig = gpd.read_file(f"{data_path}")
    geo_nig.drop(
        columns=[
            "admin2AltN",
            "admin2Al_1",
            "ValidTo",
            "date",
            "validOn",
            "Shape_Leng",
            "Shape_Area",
            "admin0Name",
            "admin0Pcod",
        ],
        axis=1,
        inplace=True,
    )
    return geo_nig


def check_file_existence(file_path: str) -> bool:
    """
    Check if a file exists at the given file path.

    Parameters:
        file_path (str): The path to the file to be checked.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    path = Path(file_path)
    return path.exists()


def extract_timescales(data: pd.DataFrame):
    """
    Extract day, month, and year from the 'date' column of the DataFrame.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the 'date' column.

    Returns:
        None. Modifies the DataFrame in-place by adding 'day', 'month', and 'year' columns.
    """
    data["date"] = pd.to_datetime(data["date"])

    # Extract day of the year
    data["day"] = data["date"].dt.dayofyear
    data["month"] = data["date"].dt.month
    data["year"] = data["date"].dt.year


def thresholds_saver_loader(
    file_path: Union[str, Path], data: Any = None, action: str = "save"
):
    """
    Save or load data using pickle to/from a specified file path.

    Parameters:
        file_path (Union[str, Path]): The path to the file to be saved or loaded.
        data (Any, optional): The data to be saved. Required when action is "save".
        action (str, optional): The action to perform. Options: "save" or "load".

    Returns:
        Any: Loaded data if action is "load".
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)

    filename = file_path.name
    if action == "save":
        if data is None:
            print("No data provided to save.")
            return
        # Save the data to a file
        with open(f"{file_path}", "wb") as file:
            pickle.dump(data, file)
            print(f"{'=' * 3 }> Data saved to {file_path.parent} as {filename} [DONE]")
    elif action == "load":
        try:
            # Load the data from the file
            with open(f"{file_path}", "rb") as file:
                loaded_data = pickle.load(file)
                print(
                    f"{'=' * 3 }> [LOADING] {filename} from {file_path.parent} [DONE]"
                )
                return loaded_data
        except FileNotFoundError:
            print(f"File {filename} not found.")
    else:
        print("Invalid action. Use 'save' or 'load'.")


def compute_years_daily_averaging_threshold_per_grid(
    data: pd.DataFrame, event: str, geo_columns: list, window: int
):
    """
    Compute the rolling daily averages of an event per grid coordinate for each year.

    Parameters:
        data (pd.DataFrame): The DataFrame containing the weather event data.
        event (str): The name of the weather event column.
        geo_columns (list): List of columns representing the grid coordinates.
        window (int): The rolling window size.

    Returns:
        dict: A dictionary containing rolling daily averages per grid coordinate.
    """
    unique_paired_geo_coordinates = data.drop_duplicates(subset=geo_columns)[
        geo_columns
    ].values.tolist()

    geo_years_daily_rolling_averages = {}
    for longitude, latitude in unique_paired_geo_coordinates:
        filtered_data = data[(data.lon == longitude) & (data.lat == latitude)].copy()

        # Extract years from the 'date' column
        filtered_data["year"] = filtered_data["date"].dt.year

        unique_years, years_rolling_averages = list(filtered_data.year.unique()), {}
        for year in unique_years:
            year_rolling_daily_average = (
                filtered_data[filtered_data.year == year][event]
                .rolling(window=window, min_periods=1, center=True)
                .mean()
            )
            years_rolling_averages[year] = year_rolling_daily_average.fillna(0).tolist()

        lists = list(years_rolling_averages.values())

        # Calculate the mean of corresponding indices
        mean_values = [
            np.nanmean(values) for values in zip_longest(*lists, fillvalue=0)
        ]
        geo_years_daily_rolling_averages[f"{longitude}-{latitude}"] = mean_values
    return geo_years_daily_rolling_averages


def severity_measure(data: Dict[int, float], days_param: int = 3) -> Dict[int, float]:
    """
    Calculate severity measure for consecutive positive values.

    Parameters:
        data (Dict[int, float]): A dictionary of values indexed by day.
        days_param (int): The minimum number of consecutive positive days to calculate the severity. Defaults to 3.

    Returns:
        Dict[int, float]: A dictionary containing severity values indexed by day.
    """
    impact = {}

    for i, value in data.items():
        if value <= 0:
            impact[i] = 0
        else:
            consecutive_days_sum = value
            consecutive_days_count = 1

            j = i + 1
            while j in data and data[j] > 0:
                consecutive_days_sum += data[j]
                consecutive_days_count += 1
                if consecutive_days_count >= days_param:
                    impact[i] = consecutive_days_sum
                    for k in range(i + 1, j + 1):
                        impact[k] = consecutive_days_sum
                j += 1

    return impact


def assign_severity(row: Dict[str, Any], measure: Dict[int, float]) -> float:
    """
    Assign severity to a row based on the severity measure.

    Parameters:
        row (Dict[str, Any]): The row of data containing 'day' information.
        measure (Dict[int, float]): The severity measure dictionary.

    Returns:
        float: The assigned severity value.
    """
    day = row["day"]
    if day in measure:
        return measure[day]
    return 1.0


def initialize_features_columns(data: pd.DataFrame) -> None:
    """
    Initialize severity and ranking columns based on the 'extreme' column values.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing weather event data.

    Returns:
        None. Modifies the input DataFrame by setting 'severity' and 'ranking' columns based on 'extreme' column values.
    """
    # Set the 'severity' and 'ranking' column to 0 for rows where 'extreme' is False
    data.loc[data["extreme"] == False, "severity"] = 0
    data.loc[data["extreme"] == False, "ranking"] = 0


def create_severity_value(
    data: pd.DataFrame, year: int, geo_columns: List[str], days_param: int
) -> pd.DataFrame:
    """
    Create and compute severity values for extreme weather events in a given year.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing weather event data.
        year (int): The year for which severity values are computed.
        geo_columns (List[str]): List of column names representing geographical coordinates.
        days_param (int): Parameter for computing severity.

    Returns:
        pd.DataFrame: A DataFrame containing computed severity and ranking values for the given year.
    """
    year_data = data[data.year == year].copy()
    longitude_column, latitude_column = geo_columns

    unique_paired_geo_coordinates = data.drop_duplicates(subset=geo_columns)[
        geo_columns
    ].values.tolist()

    for longitude, latitude in unique_paired_geo_coordinates:
        # Filter data by longitude and latitude unique pair
        layer_data = year_data[
            (year_data[longitude_column] == longitude)
            & (year_data[latitude_column] == latitude)
        ][["day", "delta", "severity", "ranking"]].copy()

        # Retain the indices of the filtered data from the main data
        layer_data_indices = year_data.loc[
            (year_data[longitude_column] == longitude)
            & (year_data[latitude_column] == latitude)
        ].index

        # Compute severity for the filtered dataset
        severity_column = layer_data["severity"]
        extreme_severity_nan_indices = severity_column.index[severity_column.isna()]
        severe_days_delta_data = layer_data.loc[extreme_severity_nan_indices, :]
        severe_days_delta = severe_days_delta_data.set_index("day")["delta"].to_dict()

        layer_measures = (
            severe_days_delta_data[["day", "severity"]]
            .apply(
                assign_severity,
                args=(severity_measure(severe_days_delta, days_param),),
                axis=1,
            )
            .tolist()
        )

        layer_ranking = [2 if measure > 1 else 1 for measure in layer_measures]

        # Sanity checks
        assert layer_data.severity.isna().sum() == len(layer_measures)
        assert len(layer_data) == len(layer_data_indices)

        # Impute computed values for filtered dataset with sanity check
        layer_data.loc[extreme_severity_nan_indices, "severity"] = layer_measures
        layer_data.loc[extreme_severity_nan_indices, "ranking"] = layer_ranking
        assert layer_data.severity.isna().sum() == layer_data.ranking.isna().sum() == 0

        # Set the indices of the filtered dataset to its parent indices with sanity check
        layer_data.set_index(pd.Index(layer_data_indices), inplace=True)
        assert list(layer_data.index) == list(
            data.loc[layer_data_indices, "severity"].index
        )

        # Update the severity/ranking values of the filtered dataset in the year dataset
        year_data.loc[layer_data_indices, ["severity", "ranking"]] = layer_data[
            ["severity", "ranking"]
        ]

    year_severity_ranking = year_data.loc[:, ["severity", "ranking"]]
    del year_data
    return year_severity_ranking


def compute_severity_ranking(data: pd.DataFrame, event: str, days_param: int = 3):
    """
    Compute severity and ranking measures for extreme weather events in the provided data.

    Parameters:
        data (pd.DataFrame): The input DataFrame containing weather event data.
        event (str): The name of the weather event column.
        days_param (int, optional): Parameter for computing severity. Default is 3.

    Returns:
        None
    """
    data_years = list(data.year.unique())

    for year in data_years:
        year_severity_ranking = create_severity_value(
            data, year, GEO_COLUMNS, days_param
        )
        data.loc[
            year_severity_ranking.index, ["severity", "ranking"]
        ] = year_severity_ranking[["severity", "ranking"]]


def batching(container: List, batch_size: int) -> List[List]:
    """
    Split a container into batches of a specified size.

    Parameters:
        container (list): The container to be split.
        batch_size (int): The size of each batch.

    Returns:
        list of lists: List of batches, each containing a subset of the input container.
    """
    batches = []
    for indx in range(0, len(container), batch_size):
        batch = container[indx : indx + batch_size]
        batches.append(batch)
    return batches


def plot_heatmap(
    matrix,
    title,
    save_path,
    figsize=(8, 6),
    cmap="coolwarm",
    annot=False,
    fmt=".1f",
    save=False,
):
    """
    Plots a heatmap based on the given matrix (numpy array).

    Parameters:
    - matrix (numpy array): The matrix containing the values to be plotted.
    - title (str): Title of the heatmap.
    - save_path (str): Path where the heatmap visualization will be saved.
    - figsize (tuple): Figure size. Default is (8, 6).
    - cmap (str): Color map used for the heatmap. Default is 'coolwarm'.
    - annot (bool): Whether to annotate each cell with their value. Default is False.
    - fmt (str): String formatting code to use when adding annotations. Default is ".1f".

    Returns:
    None. Displays and saves the heatmap visualization.
    """

    mask = np.triu(np.ones_like(matrix, dtype=bool))

    plt.figure(figsize=figsize)
    sns.heatmap(matrix, mask=mask, annot=annot, fmt=fmt, cmap=cmap)
    plt.title(title, size=10)
    if save:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")

    plt.show()


def batching(list_of_elements: List, batch_size: int) -> List[List]:
    """
    Split a list_of_elements into batches of a specified size.

    Parameters:
        list_of_elements (list): The list_of_elements to be split.
        batch_size (int): The size of each batch.

    Returns:
        list of lists: List of batches, each containing a subset of the input list_of_elements.
    """
    batches = []
    for indx in range(0, len(list_of_elements), batch_size):
        batch = list_of_elements[indx : indx + batch_size]
        batches.append(batch)
    return batches


def get_weather_data_open_meteo(
    latitude: float, longitude: float, start: str, end: str = None
) -> pd.DataFrame:
    """
    Fetches weather data from the Open-Meteo API for a specified location and time range.

    This function constructs a URL using the provided latitude, longitude, start date,
    and end date, to fetch daily weather data including maximum, minimum, and mean
    temperatures, as well as total precipitation. The fetched data is processed and
    returned as a DataFrame.

    Parameters:
        latitude (float): The latitude of the location for weather data retrieval.
        longitude (float): The longitude of the location for weather data retrieval.
        start (str): The start date of the data range in 'YYYY-MM-DD' format.
        end (str)(optional): The end date of the data range in 'YYYY-MM-DD' format.

    Returns:
        pd.DataFrame: A DataFrame containing processed weather data with columns for:
            - date (str): The date of the weather data in 'YYYY-MM-DD' format.
            - temperature_2m_max (float): Maximum 2-meter temperature in Celsius.
            - temperature_2m_min (float): Minimum 2-meter temperature in Celsius.
            - temperature_2m_mean (float): Mean 2-meter temperature in Celsius.
            - precipitation_sum (float): Total daily precipitation in millimeters.
    """
    # Get data for only one day
    if end is None:
        end = start

    link = f"https://archive-api.open-meteo.com/v1/archive?latitude={latitude}&longitude={longitude}&start_date={start}&end_date={end}&daily=temperature_2m_max,temperature_2m_min,temperature_2m_mean,precipitation_sum&timezone=auto"

    try:
        # Fetch weather data from the provided link
        response = requests.get(link, timeout=5)
        weather_data = response.json()

        # Create an empty DataFrame to store the processed data
        combined_df = pd.DataFrame()

        # Iterate through each data point and add it to the DataFrame
        for key, value in weather_data["daily"].items():
            combined_df[key] = value

        # Rename the 'time' column to 'date'
        combined_df.rename(columns={"time": "date"}, inplace=True)
        combined_df.insert(0, "lat", weather_data["latitude"], True)
        combined_df.insert(1, "lon", weather_data["longitude"], True)

        return combined_df

    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_weather_for_household(hh_data: pd.DataFrame) -> pd.DataFrame:
    """
    Fetches weather data for each household's location and merges it with household data.

    This function takes household data containing latitude, longitude, and date information,
    fetches weather data for each household's location and date, and combines it with the
    original household data. The weather data includes maximum, minimum, and mean temperatures,
    as well as total daily precipitation.

    Parameters:
        hh_data (pd.DataFrame): Household data containing 'lat', 'lon', and 'date' columns.

    Returns:
        pd.DataFrame: A DataFrame containing combined household and weather data
    """
    # Extract necessary columns and preprocess the date
    hh_data = hh_data[["lat", "lon", "date"]]
    hh_data.loc[:, "date"] = pd.to_datetime(hh_data["date"]).dt.date
    hh_data = hh_data.drop_duplicates()
    hh_data.set_index("date", inplace=True)

    # Fetch weather data for each household's location and date
    weather_dataframes = pd.DataFrame()
    for index, row in hh_data.iterrows():
        weather_data = get_weather_data_open_meteo(row["lat"], row["lon"], index)
        weather_dataframes = pd.concat(
            [weather_dataframes, weather_data], ignore_index=True
        )

    # Reset index of household data and select relevant columns from weather data
    hh_data = hh_data.reset_index()
    weather_dataframes = weather_dataframes[
        [
            "temperature_2m_max",
            "temperature_2m_min",
            "temperature_2m_mean",
            "precipitation_sum",
        ]
    ]

    # Combine household data with weather data
    weather_data_combined = pd.concat([hh_data, weather_dataframes], axis=1)
    return weather_data_combined


def preprocess_weather_datasets(
    precip_data: pd.DataFrame,
    temp_data: pd.DataFrame,
    needed_cols_precip: List[str] = [
        "date",
        "lat",
        "lon",
        "precipitation",
        "month",
        "year",
        "delta",
        "SPI",
    ],
    needed_cols_temp: List[str] = [
        "date",
        "lat",
        "lon",
        "temperature",
        "month",
        "year",
        "delta",
    ],
    cols_rename_dict: Dict[str, Dict[str, str]] = {
        "precipitation": {"delta": "heavy_rain_index", "SPI": "spi_index"},
        "temperature": {"delta": "heatwave_index"},
    },
    non_float_cols: List[str] = ["date", "month", "year"],
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Preprocesses the precipitation and temperature datasets.

    This function preprocesses the precipitation and temperature datasets by selecting
    only the needed columns, rounding the float columns to 2 decimals, and renaming
    the columns.

    Parameters:
        precip_data (pd.DataFrame): The precipitation dataset.
        temp_data (pd.DataFrame): The temperature dataset.
        needed_cols_precip (List[str]): The list of needed columns for the precipitation dataset.
        needed_cols_temp (List[str]): The list of needed columns for the temperature dataset.
        cols_rename_dict (Dict[str, Dict[str, str]]): The dictionary containing the columns to be renamed.

    Returns:
        Tuple[pd.DataFrame, pd.DataFrame]: The preprocessed precipitation and temperature datasets.
    """
    # Select only needed columns
    precip_data = precip_data[needed_cols_precip]
    temp_data = temp_data[needed_cols_temp]

    # Round all float cols to 2 decimals
    float_cols_precip = list(set(needed_cols_precip) - non_float_cols)
    float_cols_temp = list(set(needed_cols_temp) - non_float_cols)

    for col in float_cols_precip:
        precip_data[col] = precip_data[col].round(1)

    for col in float_cols_temp:
        temp_data[col] = temp_data[col].round(1)

    # Rename columns
    for key in cols_rename_dict.keys():
        if key == "precipitation":
            precip_data = precip_data.rename(columns=cols_rename_dict[key])
        else:
            temp_data = temp_data.rename(columns=cols_rename_dict[key])

    return precip_data, temp_data
