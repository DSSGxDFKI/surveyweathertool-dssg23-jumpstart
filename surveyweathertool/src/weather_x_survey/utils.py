import pandas as pd


def read_survey_data(survey_csv_path):
    """
    Reads any survey data with geoinformation from a CSV file, renames some columns, sorts by date, removes NaN values, and resets the index.

    Parameters:
    survey_csv_path: str
        The path to the CSV file containing the household geoinformation.

    Returns:
    hh_df: DataFrame
        The preprocessed household survey data.
    """
    hh_df = pd.read_csv(f"{survey_csv_path}")
    hh_df.rename(columns={"latitude": "lat", "longitude": "lon"}, inplace=True)
    hh_df["date"] = pd.to_datetime(hh_df["date"])
    hh_df.sort_values(by=["date"], ascending=False, inplace=True)
    hh_df.dropna(inplace=True)
    hh_df.reset_index(drop=True, inplace=True)
    return hh_df


def filter_weather_data(file_path, years=None):
    """
    Reads a weather data CSV file, cleans and formats the data, and optionally filters it by year.

    Parameters:
    file_path: str
        The path to the CSV file containing the weather data.
    years: int, list, or tuple, optional
        The year or range of years to filter the data by. If an int is passed, the data will be filtered for that specific year.
        If a list or tuple of two elements is passed, it will be interpreted as the start and end years of the range (inclusive).
        If no value is passed, no filtering will be performed.

    Returns:
    DataFrame
        The cleaned and optionally filtered weather data.
    """
    weather_data = pd.read_csv(file_path)
    weather_data["date"] = pd.to_datetime(weather_data["time"])
    weather_data.drop(columns=["time"], inplace=True)
    # Group by date, lat, lon and take the mean of any duplicate entries
    weather_data = weather_data.groupby(["date", "lat", "lon"]).mean().reset_index()

    if type(years) == int:
        start_year = end_year = years
    elif type(years) in (list, tuple) and len(years) == 2:
        start_year, end_year = years
    else:
        return weather_data

    # Filter for the selected year or range of years
    mask = (weather_data["date"].dt.year >= start_year) & (
        weather_data["date"].dt.year <= end_year
    )
    weather_data = weather_data.loc[mask]
    weather_data.reset_index(drop=True, inplace=True)
    return weather_data
