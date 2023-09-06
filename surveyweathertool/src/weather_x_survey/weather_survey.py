import numpy as np
import datetime
import pandas as pd
import geopandas as gpd
from sklearn.neighbors import NearestNeighbors
from src.survey.helper import export_fn
from src.weather.weather_pipeline import (
    convert_map_crs,
    convert_point_crs,
)


def get_nearest_points(hh_df, weather_df, n_neighbors=4):
    """
    For each household, find the n nearest points in the weather grid.

    Parameters:
    hh_df: DataFrame
        Household data, including 'lat', 'lon' columns.
    weather_df: DataFrame
        Weather grid data, including 'lat', 'lon' columns.
    n_neighbors: int
        The number of nearest weather grid points to find for each household.

    Returns:
    DataFrame
        A new DataFrame with the same index as hh_df, and with two additional columns:
        'nearest_points' - list of indices of the nearest points in weather_df,
        'distances' - list of distances to the nearest points.
    """
    # Create a NearestNeighbors model
    nbrs = NearestNeighbors(n_neighbors=n_neighbors, algorithm="ball_tree")

    # Fit the model to the weather grid data
    nbrs.fit(weather_df[["lon", "lat"]])

    # Find the nearest weather grid points for each household
    distances, indices = nbrs.kneighbors(hh_df[["lon", "lat"]])

    # Create a new DataFrame with the results
    nearest_df = pd.DataFrame(
        {"nearest_points": indices.tolist(), "distances": distances.tolist()},
        index=hh_df.index,
    )

    return nearest_df


def calculate_weights(nearest_df):
    """
    Calculate the weights for the inverse distance weighting interpolation.

    Parameters:
    nearest_df: DataFrame
        DataFrame with 'nearest_points' and 'distances' columns, as returned by get_nearest_points().

    Returns:
    DataFrame
        A new DataFrame with the same index as nearest_df, and with an additional column 'weights'.
    """
    # Calculate the weights based on the inverse of the distance
    weights = nearest_df["distances"].apply(
        lambda distances: [1 / d for d in distances]
    )

    # Normalize the weights so that they sum to 1
    weights = weights.apply(lambda weights: [w / sum(weights) for w in weights])

    # Add the weights to the DataFrame
    nearest_df["weights"] = weights

    return nearest_df


def interpolate_values(weighted_nearest_df, weather_df, value_cols):
    """
    Interpolate the values for the households based on the weights of the nearest points.

    Parameters:
    weighted_nearest_df: DataFrame
        DataFrame with 'nearest_points' and 'weights' columns, as returned by calculate_weights().
    weather_df: DataFrame
        The weather DataFrame with the values to interpolate.
    value_cols: list of str
        The names of the columns in weather_df that contains the values to interpolate.

    Returns:
    DataFrame
        A new DataFrame with the interpolated values for each household.
    """
    if isinstance(value_cols, str):
        value_cols = [value_cols]

    interpolated_values = []

    # Iterate over each row in the DataFrame
    for idx, row in weighted_nearest_df.iterrows():
        # Get the indices of the nearest points
        nearest_indices = row["nearest_points"]

        # Get the weights for the interpolation
        weights = row["weights"]

        # Get the corresponding values from the weather DataFrame
        values = weather_df.loc[nearest_indices, value_cols]

        # Calculate the interpolated values as the weighted average of the values
        interpolated_row_values = np.average(values, weights=weights, axis=0)

        # Append the dictionary to the list
        interpolated_values.append(interpolated_row_values)

    # Create a new DataFrame with the interpolated values
    interpolated_df = pd.DataFrame(
        interpolated_values, columns=value_cols, index=weighted_nearest_df.index
    )

    return interpolated_df


def get_weather_for_household_survey(
    household_df, weather_df, value_col, n_neighbors=4
):
    """
    Get the interpolated weather data for each household on the day of the survey.

    Parameters:
    household_df: DataFrame
        Household survey data, including 'date', 'lat', 'lon' columns.
    weather_df: DataFrame
        Daily weather data, including 'date', 'lat', 'lon' and 'precipitation' columns.
    value_col: str
        The name of the column in weather_df that contains the values to interpolate.
    n_neighbors: int
        The number of nearest weather points to use for interpolation.

    Returns:
    DataFrame
        A new DataFrame with the interpolated weather data for each household.
    """
    hh_df = household_df.copy()
    interpolated_dfs = []  # List to store the interpolated data for each date

    # Loop over unique dates in the household survey data
    for date in hh_df["date"].unique():
        # Select the household surveys for this date
        hh_df_date = hh_df[hh_df["date"] == date]

        # Select the weather data for this date and reset index
        weather_df_date = weather_df[weather_df["date"] == date].reset_index(drop=True)

        if len(weather_df_date) == 0:
            print(f"WARNING: For the date {date} there is no weather data!")

        

        # Calculate the nearest points and distances
        nearest_df = get_nearest_points(hh_df_date, weather_df_date, n_neighbors)

        # Calculate the weights for interpolation
        weighted_nearest_df = calculate_weights(nearest_df)

        # Interpolate the weather data
        interpolated_df_date = interpolate_values(
            weighted_nearest_df, weather_df_date, value_col
        )

        # Append the interpolated data for this date to the list
        interpolated_dfs.append(interpolated_df_date)

    # Concatenate the interpolated data for all dates
    interpolated_df = pd.concat(interpolated_dfs)

    return interpolated_df


def get_monthly_weather_for_household_survey(
    household_df, weather_df, value_col, n_neighbors=4
):
    """
    Get the interpolated weather data for each household for the month of the survey.

    Parameters:
    household_df: DataFrame
        Household survey data, including 'date', 'lat', 'lon' columns.
    weather_df: DataFrame
        Monthly weather data, including 'year', 'month', 'lat', 'lon' and 'precipitation' columns.
    value_col: str
        The name of the column in weather_df that contains the values to interpolate.
    n_neighbors: int
        The number of nearest weather points to use for interpolation.

    Returns:
    DataFrame
        A new DataFrame with the interpolated weather data for each household.
    """
    hh_df = household_df.copy()
    interpolated_dfs = []  # List to store the interpolated data for each date
    col_name = "monthly_avg_" + value_col

    # Extract year and month from the household survey data
    hh_df["year"] = hh_df["date"].dt.year
    hh_df["month"] = hh_df["date"].dt.month

    # Loop over unique year-month pairs in the household survey data
    for year, month in hh_df[["year", "month"]].drop_duplicates().values:
        # Select the household surveys for this month
        hh_df_month = hh_df[(hh_df["year"] == year) & (hh_df["month"] == month)]

        # Select the weather data for this month and reset index
        weather_df_month = weather_df[
            (weather_df["year"] == year) & (weather_df["month"] == month)
        ].reset_index(drop=True)

        # Calculate the nearest points and distances
        nearest_df = get_nearest_points(hh_df_month, weather_df_month, n_neighbors)

        # Calculate the weights for interpolation
        weighted_nearest_df = calculate_weights(nearest_df)

        # Interpolate the weather data
        interpolated_df_month = interpolate_values(
            weighted_nearest_df, weather_df_month, value_col
        )

        # Add the year and month columns to the interpolated data
        # interpolated_df_month['year'] = year
        # interpolated_df_month['month'] = month

        # Append the interpolated data for this month to the list
        interpolated_dfs.append(interpolated_df_month)

    # Concatenate the interpolated data for all months
    interpolated_df = pd.concat(interpolated_dfs)

    # Change column name
    interpolated_df.rename(columns={value_col: col_name}, inplace=True)

    return interpolated_df


def get_seasonal_weather_for_household_survey(
    household_df, weather_df, value_col, n_neighbors=4
):
    """
    Get the interpolated weather data for each household for the season of the survey.

    Parameters:
    household_df: DataFrame
        Household survey data, including 'date', 'lat', 'lon' columns.
    weather_df: DataFrame
        Seasonal weather data, including 'year', 'season', 'lat', 'lon' and 'precipitation' columns.
    value_col: str
        The name of the column(s) in weather_df that contains the values to interpolate.
    n_neighbors: int
        The number of nearest weather points to use for interpolation.

    Returns:
    DataFrame
        A new DataFrame with the interpolated weather data for each household.
    """

    def assign_season(date):
        """
        Assign a season to a date.

        Parameters:
        date: datetime
            The date to assign a season to.

        Returns:
        str
            The season ('winter', 'spring', 'summer', 'fall') that the date falls in.
        """
        month = date.month

        if 3 <= month <= 5:
            return "spring"
        elif 6 <= month <= 8:
            return "summer"
        elif 9 <= month <= 11:
            return "fall"
        else:
            return "winter"
        
    def assign_season_nigeria(date: datetime) -> str:
        """
        Assign a season to a date (Nigeria specific).

        Parameters:
        date: datetime
            The date to assign a season to.

        Returns:
        str
            The season ('wet' or 'dry') that the date falls in.
        """
        month = date.month

        if month in [5,6,7,8,9]:
            return "wet"
        else:
            return "dry"

    interpolated_dfs = []  # List to store the interpolated data for each date
    col_name = (
        "seasonal_avg_" + value_col
    )  # Tracking column names to rename column in finished df

    # Extract year and season from the household survey data
    hh_df = household_df.copy()
    hh_df["year"] = hh_df["date"].dt.year
    hh_df["date"] = hh_df["date"].dt.date
    hh_df["season"] = hh_df["date"].apply(assign_season_nigeria)

    # Extract season from weather data
    weather_df["date"] = weather_df["date"].dt.date
    weather_df["season"] = weather_df["date"].apply(assign_season_nigeria)

    # Loop over unique year-season pairs in the household survey data
    for year, season in hh_df[["year", "season"]].drop_duplicates().values:
        # Select the household surveys for this season
        hh_df_season = hh_df[(hh_df["year"] == year) & (hh_df["season"] == season)]

        # Select the weather data for this season and reset index
        weather_df_season = weather_df[
            (weather_df["year"] == year) & (weather_df["season"] == season)
        ].reset_index(drop=True)

        # Calculate the nearest points and distances
        nearest_df = get_nearest_points(hh_df_season, weather_df_season, n_neighbors)

        # Calculate the weights for interpolation
        weighted_nearest_df = calculate_weights(nearest_df)

        # Interpolate the weather data
        interpolated_df_season = interpolate_values(
            weighted_nearest_df, weather_df_season, value_col
        )

        # Add the year and season columns to the interpolated data
        # interpolated_df_season['year'] = year
        interpolated_df_season["season"] = season

        # Append the interpolated data for this season to the list
        interpolated_dfs.append(interpolated_df_season)

    # Concatenate the interpolated data for all seasons
    interpolated_df = pd.concat(interpolated_dfs)

    # Change column name
    interpolated_df.rename(columns={value_col: col_name}, inplace=True)

    return interpolated_df


def get_yearly_weather_for_household_survey(
    household_df, weather_df, value_col, n_neighbors=4
):
    """
    Get the interpolated weather data for each household for the year of the survey.

    Parameters:
    household_df: DataFrame
        Household survey data, including 'date', 'lat', 'lon' columns.
    weather_df: DataFrame
        Yearly weather data, including 'year', 'lat', 'lon' and 'precipitation' columns.
    value_col: str
        The name of the column(s) in weather_df that contains the values to interpolate.
    n_neighbors: int
        The number of nearest weather points to use for interpolation.

    Returns:
    DataFrame
        A new DataFrame with the interpolated weather data for each household.
    """
    interpolated_dfs = []  # List to store the interpolated data for each date
    hh_df = household_df.copy()
    col_name = "yearly_avg_" + value_col

    # Extract year from the household survey data
    hh_df["year"] = hh_df["date"].dt.year

    # Loop over unique years in the household survey data
    for year in hh_df["year"].unique():
        # Select the household surveys for this year
        hh_df_year = hh_df[hh_df["year"] == year]

        # Select the weather data for this year and reset index
        weather_df_year = weather_df[weather_df["year"] == year].reset_index(drop=True)

        # Calculate the nearest points and distances
        nearest_df = get_nearest_points(hh_df_year, weather_df_year, n_neighbors)

        # Calculate the weights for interpolation
        weighted_nearest_df = calculate_weights(nearest_df)

        # Interpolate the weather data
        interpolated_df_year = interpolate_values(
            weighted_nearest_df, weather_df_year, value_col
        )

        # Add the year column to the interpolated data
        # interpolated_df_year["year"] = year

        # Append the interpolated data for this year to the list
        interpolated_dfs.append(interpolated_df_year)

    # Concatenate the interpolated data for all years
    interpolated_df = pd.concat(interpolated_dfs)

    # Change column name
    interpolated_df.rename(columns={value_col: col_name}, inplace=True)

    return interpolated_df


def merge_weather_household(
    hh_df,
    weather_df,
    column_name,
):
    """
    Merge weather data from different time periods (monthly, seasonal, yearly) for different metrics (precipitation, temperature, etc. )
    into a single DataFrame. The merged DataFrame will contain weather data for each household, with separate columns for each time
    period and metric.

    Parameters:
    hh_df: DataFrame
        Household survey data, including 'date', 'lat', 'lon' columns.
    weather_df: DataFrame
        Particular weather dataframe with geographic and weather information to aggregate

    Returns:
    DataFrame
        A merged DataFrame containing weather data for each household for different time periods and metrics.
    """
    
    # Get weather data for each time period and metric, and rename columns
    day_agg_survey_df = get_weather_for_household_survey(
        hh_df, 
        weather_df, 
        value_col=column_name
    )

    monthly_agg_df = get_monthly_weather_for_household_survey(
        hh_df,
        weather_df,
        value_col=column_name
    )

    # For more features, call get_seasonal_weather_for_household_survey & get_yearly_weather_for_household_survey...
    # Merge all the data together, assuming they have the same index
    merged_df = pd.concat(
        [
            hh_df,
            day_agg_survey_df,
            monthly_agg_df
        ],
        axis=1,
    )

    # Add date columns (and drop duplicate season columns)
    merged_df["month"] = hh_df["date"].dt.month
    merged_df["year"] = hh_df["date"].dt.year
 
    cols = [
        "lat",
        "lon",
        "date",
        column_name,
        "monthly_avg_" + column_name,
    ]

    merged_df = merged_df[cols]

    return merged_df


def merge_survey_weather_hh_level(
    survey_filepath: str,
    weather_filepath: str,
    export_flag: True,
    export_format: str,
    export_path: str,
) -> pd.DataFrame:
    weather = pd.read_csv(weather_filepath)
    weather = weather.drop_duplicates()  # TODO dont understand why there are still
    # duplicates being produced in pipeline? or is this just in jama handover csv
    # file??
    weather = weather.convert_dtypes()
    weather["date"] = pd.to_datetime(weather["date"])
    weather = weather.set_index(["hhid", "wave", "date"])  # , 'date'
    weather = weather.sort_index()

    # Add visit column in the weather data
    weather["visit"] = 1  # Default fill to visit 1

    visited = set()
    for current_hhid, current_wave, current_date in weather.index:
        if (current_hhid, current_wave) not in visited:
            visited.update(
                [(current_hhid, current_wave)]
            )  # Add to visited if already have (hhid, wave)
            # information
        else:
            weather.loc[(current_hhid, current_wave, current_date), "visit"] = 2
            continue
    ####

    # Set new index
    new_index = ["hhid", "wave", "visit"]
    weather = weather.reset_index()
    weather = weather.set_index(new_index)

    # Survey
    survey = pd.read_pickle(survey_filepath)
    survey = survey.drop(columns=["date"])

    # Combine
    survey_weather = survey.join(weather, how="left", validate="m:1")
    survey_weather = survey_weather.reset_index()
    survey_weather = survey_weather.set_index(["hhid", "indiv", "wave", "visit"])

    # Export
    if export_flag:
        export_name = "survey_weather"
        export_fn(survey_weather, f"{export_path}/{export_name}", export_format)

    return survey_weather


def combine_with_poverty_index(
    map_df: gpd.GeoDataFrame,
    household_df: gpd.GeoDataFrame,
    col_dissolve: str,
    wave: int = 1,
    poverty_index_col_name: str = "unicef_poverty_index",
    method: str = "intersects",
    epsg: int = 4326,
):
    """
    Function to combine two GeoDataFrames based on a spatial join operation and computes the
    aggregate mean of the poverty index for households in each region.

    Parameters
    ----------
    map_df : geopandas.GeoDataFrame
        The GeoDataFrame with the geometry column to be used for the spatial join.
    household_df : geopandas.GeoDataFrame
        The GeoDataFrame with household data, including poverty index.
    col_dissolve : str
        The column name in map_df used to dissolve the geometry into unique polygons.
    wave: int
        The wave in the survey to consider
    poverty_index_col_name: str
        The column name in household_df that has poverty index
    method : str, optional
        The method to be used for the spatial join operation. It could be "intersects", "within", "contains", etc.
        Default is "intersects".
    epsg
        EPSG code to set the Coordinate Reference System (CRS) for the data

    Returns
    -------
    admin_db : geopandas.GeoDataFrame
        The GeoDataFrame resulting from the spatial join with aggregate mean poverty index.

    """
    if (
        "wave" not in household_df.columns
        or poverty_index_col_name not in household_df.columns
    ):
        raise ValueError(
            "Required columns (wave or unicef_poverty_index) are missing from the dataframe."
        )

    household_subset_df = household_df[
        household_df["wave"] == wave
    ].copy()  # subset the wave
    household_subset_df = convert_point_crs(
        df=household_subset_df, target_epsg=epsg
    )  # convert to geo dataframe
    dissolved_df = map_df.dissolve(col_dissolve).reset_index()
    admin_db = gpd.sjoin(dissolved_df, household_subset_df, predicate=method)

    # Calculate aggregate mean of the poverty index for each region
    admin_db = (
        admin_db.groupby(col_dissolve)
        .agg({poverty_index_col_name: "mean", "geometry": "first"})
        .reset_index()
    )
    admin_db = convert_map_crs(geo_df=admin_db, epsg=epsg)
    return admin_db
