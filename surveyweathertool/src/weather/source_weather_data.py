## Sourcing and preprocessing temperature and precipitation data

# Import statements
import os
import time
import pandas as pd
from pathlib import Path
from src.survey.helper import dataframe_reader
from src.weather.weather_pipeline import calculate_SPI
from src.weather.utils import read_shape_file, ncToCSV, preprocess_weather_datasets
from src.weather.weather_pipeline import interpolate_data_for_all_dates, clip_data
from src.weather.weather_pipeline import heatwave_heavy_rainfall_indicators
from src.weather.constants import *


def preprocess_data(source_path, dest_path, weather, coordinate_limits):
    """
    Preprocess weather data by filling missing values, grouping, and saving as Pickle files.

    Parameters:
    source_path (str): Directory containing source CSV files.
    dest_path (str): Directory where processed files will be saved.
    coordinate_limits (list): List of latitude and longitude coordinate limits.

    Notes:
    This function assumes that the CSV files have columns 'lat', 'lon', and 'precip'.
    """
    print("Start preprocessing the weather data")

    print(f"Check if {dest_path} already exists, if not create it")
    os.makedirs(dest_path, exist_ok=True)

    files_to_process = []

    for filename in os.listdir(source_path):
        print(f"Preprocess the file {filename}")
        # Convert NetCDF to CSV and filter based on coordinates
        ncToCSV(
            source_path.joinpath(filename),
            dest_path.joinpath(Path(filename[:-3] + ".csv")),
            coordinate_limits,
        )
        df = pd.read_csv(dest_path.joinpath(Path(filename[:-3] + ".csv")))

        # Handle missing values and filter data
        # Get all the files where the missing data for a location is less than 365 days in an year
        filteredDF = df[df.iloc[:, 2].isna() == True]
        filteredDF = filteredDF.fillna(0)
        grouping_columns = list(filteredDF.iloc[:, :3].columns)
        filteredDF = filteredDF.groupby(grouping_columns).size()
        filteredDF = filteredDF.reset_index()
        filteredDF = filteredDF[filteredDF[0] < 365]

        if not filteredDF.empty:
            files_to_process.append(filename)

    for filename in os.listdir(dest_path):
        if filename[:-4]:
            df = pd.read_csv(dest_path.joinpath(Path(filename[:-4] + ".csv")))

            # There are very few missing values for the years 2008, 2014 and 2015 etc
            # so we filled them based on the previous day's data
            if filename in files_to_process:
                df = df.fillna(method="ffill")

            # For the stations with missing data throughout the year, we dropped them from the final dataframe
            finalDF = df.dropna()

            # Check for missing data
            no_missing_values_in_weather = finalDF[weather].isnull().sum()
            print(
                f"The number of missing values in weather is: {no_missing_values_in_weather}"
            )

            print("The final df that is being saved as pkl is:")
            print(finalDF.head())

            # Cleaned file
            finalDF.to_pickle(dest_path.joinpath(Path(filename[:-4] + ".pkl")))


def get_weather_data(
    spi_path: str,
    GEO_COLUMNS: list,
    source_weather_data: bool = False,
    nigeria_shape_path: str = None,
    data_path_temperature: str = None,
    data_path_precipitation: str = None,
    interpolate=False,
    clip=False,
):
    """
    Fetches and processes weather data based on provided file paths.
    NB: Sourcing from internet is not currently functional

    Parameters:
    -----------
    spi_path: str
        File path name to save the SPI file. if the file already don't exist, SPI will be calculated and saved again.
    nigeria_shape_path: str, optional
        Path to the Nigeria shapefile. If not provided, an attempt to source the data from the internet is made.
    data_path_temperature: str, optional
        Path to the file containing temperature data. If not provided, an attempt to source the data from the internet is made.
    data_path_precipitation: str, optional
        Path to the file containing precipitation data. If not provided, an attempt to source the data from the internet is made.

    Returns:
    --------
    tuple
        A tuple containing:
        - nigeria_shape_df: geopandas.GeoDataFrame representing the Nigeria shapefile.
        - weather_temperature_df: DataFrame containing temperature data.
        - weather_precipitation_df: DataFrame containing precipitation data.
        - weather_spi_df: DataFrame representing the calculated Standardized Precipitation Index (SPI).
    """

    if source_weather_data:
        # TODO: Actually call here than the function to properly source the data
        # TODO: Sourcing the shapefile will be a different source than the weather data, handle it differently?
        print("Start sourcing the weather data")
        raise ValueError("Sourcing data from the internet currently not available")

    else:
        # read nigeria shape file and weather data
        nigeria_shape_df = read_shape_file(data_path=nigeria_shape_path)
        weather_temperature_df = dataframe_reader(file_path=data_path_temperature)
        weather_precipitation_df = dataframe_reader(file_path=data_path_precipitation)
        print(f"**** Temperature columns: {weather_temperature_df.columns}")
        print(f"**** Precipitation columns: {weather_precipitation_df.columns}")
        print(f"**** Temperature size: {weather_temperature_df.shape}")
        print(f"**** Precipitation size: {weather_precipitation_df.shape}")

        if interpolate:  # We only interpolate temperature
            print("Started interpolation for temperature")
            start = time.time()
            weather_temperature_df = interpolate_data_for_all_dates(
                df=weather_temperature_df,
                geo_df=nigeria_shape_df,
                value_col="temperature",
                lat_res=0.1,
                lon_res=0.1,
                method="linear",
                epsg=4326,
            )
            print(f"Overal time taken by the interpolation: {time.time()-start}")

        if clip:  # We only clip for precipitation here
            print("Started clipping for precipitation")
            start = time.time()
            weather_precipitation_df = clip_data(
                df=weather_precipitation_df,
                geo_df=nigeria_shape_df,
                epsg=4326,
            )
            print(f"Overal time taken by the clipping: {time.time()-start}")

        print("==== Started Heatwave =====")
        start = time.time()
        weather_temperature_df = heatwave_heavy_rainfall_indicators(
            weather_temperature_df,
            "temperature",
            GEO_COLUMNS,
        )
        print(f"Time taken by heatwave: {time.time() - start}")
        new_start = time.time()
        weather_precipitation_df = heatwave_heavy_rainfall_indicators(
            weather_precipitation_df, "precipitation", GEO_COLUMNS, delta_param=15
        )
        print(f"Time taken by heavy rain: {time.time() - new_start}")
        print(f"Overall taken by heatwave + heavy rain: {time.time() - new_start}")
        if os.path.exists(spi_path):
            print(f"'{spi_path}' exists! Skipping SPI computation and reading SPI file")
            spi_df = dataframe_reader(file_path=spi_path)
        else:
            print("========= Started SPI computation, wait for few minutes ==========")
            start = time.time()
            spi_df = calculate_SPI(df=weather_precipitation_df)
            print(f"Overal time taken SPI computation: {time.time()-start}")

        weather_precipitation_df["SPI"] = spi_df["SPI"]

        # Preprocess the weather data before saving it
        weather_precipitation_df, weather_temperature_df = preprocess_weather_datasets(
            weather_precipitation_df, weather_temperature_df
        )

        # Save precipitation and temperature files with all of the climate indicators
        if os.path.exists(PRECIPITATION_INDICATORS):
            print(f"'{PRECIPITATION_INDICATORS}' already exists!")
        else:
            pd.to_pickle(
                weather_precipitation_df,
                PRECIPITATION_INDICATORS,
            )

        if os.path.exists(TEMPERATURE_INDICATORS):
            print(f"'{TEMPERATURE_INDICATORS}' already exists!")
        else:
            pd.to_pickle(
                weather_temperature_df,
                TEMPERATURE_INDICATORS,
            )
    return (nigeria_shape_df, weather_temperature_df, weather_precipitation_df)
