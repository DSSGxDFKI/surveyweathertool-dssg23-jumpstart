from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
import io
import pandas as pd
import streamlit as st
from PIL import Image
from pathlib import Path
from typing import List, Optional
import psutil

from src.weather.weather_pipeline import convert_point_crs


@st.cache_data
def read_logos(logos_path):
    """
    Reads and returns the STC, UNICEF, DSA, and NOAA logos from the provided path.

    Parameters:
    -----------
    logos_path : str
        The path to the directory containing the logo images.

    Returns:
    --------
    tuple of PIL.Image.Image
        The STC, UNICEF, and DSA logos as PIL Image objects.
    """
    STCimage = Image.open(f"{logos_path}/stc.png")
    UNICEFimage = Image.open(f"{logos_path}/unicef.png")
    DSAimage = Image.open(f"{logos_path}/dsa.png")
    NOAAimage = Image.open(f"{logos_path}/noaa.png")
    return STCimage, UNICEFimage, DSAimage, NOAAimage


def filter_weather(
    weather_df: pd.DataFrame, year: int, month: int = None, season: str = None
):
    """
    Filters the given DataFrame based on the provided year, month, or season.

    Parameters:
    -----------
    weather_df : pandas.DataFrame
        The DataFrame to filter.
    year : int
        The year to filter on. Can be a specific year as a string or "All Years" to include all years.
    month : int, optional
        The month to filter on. Can be a specific month as an integer (1-12) or None.
    season : str, optional
        The season to filter on. Can be a specific season as a string or None.

    Returns:
    --------
    pandas.DataFrame
        The filtered DataFrame.
    """

    weather_df = weather_df[weather_df["year"] == year]

    if month:
        weather_df = weather_df[weather_df["month"] == month]
    if season:
        weather_df = weather_df[(weather_df["season"] == season)]
    return weather_df


def filter_survey(survey_df: pd.DataFrame, wave: int = 1, target_epsg: int = 4326):
    """
    Filters the given survey DataFrame based on the provided wave.

    Parameters:
    -----------
    survey_df : pandas.DataFrame
        The DataFrame to filter.
    wave : int, Optional
        The wave to filter on. Can be a specific wave. Defaults to 1.
    Returns:
    --------
    pandas.DataFrame
        The filtered DataFrame.

    """

    survey_df.rename(columns={"latitude": "lat", "longitude": "lon"}, inplace=True)
    important_columns = [
        "hhid",
        "indiv",
        "wave",
        "visit",
        "lat",
        "lon",
        "shelter_indicator",
        "sanitation_indicator",
        "water_indicator",
        "health_indicator",
        "education_indicator",
        "nutrition_indicator",
        "non_null_count",
        "unicef_poverty_index",
    ]
    survey_df = survey_df[important_columns].copy()
    survey_df = convert_point_crs(df=survey_df, target_epsg=target_epsg).fillna(0)
    if "wave" not in survey_df.columns:
        raise ValueError("wave column doesnt exist in the survey data")
    survey_subset_df = survey_df[survey_df["wave"] == wave].copy()
    print(f"Number of unique HHs in wave: {wave}", len(survey_subset_df.hhid.unique()))
    return survey_subset_df


def check_if_df_has_lat_long(df: pd.DataFrame):
    """Checks if a dataframe has columns named "lat" and "long".

    Keyword arguments:
    df -- the dataframe to check
    """
    if "lat" not in df.columns:
        raise ValueError("Dataframe does not have a column named 'lat'.")
    if "lon" not in df.columns:
        raise ValueError("Dataframe does not have a column named 'lon'.")


def preprocess_data_input(df: pd.DataFrame) -> pd.DataFrame:
    """Lower-cases all column names and converts date column to datetime.

    Keyword arguments:
    df -- the dataframe to check
    """
    # Eliminate Whitespaces in columns
    df.columns = df.columns.str.strip()

    # Date time the date column
    df["date"] = pd.to_datetime(df["date"])

    # Drop duplications of the same location at the same day
    df.drop_duplicates(subset=["date", "lat", "lon"], inplace=True)

    return df


def preprocess_weather_data(df: pd.DataFrame) -> pd.DataFrame:
    """Lower-cases all column names, converts date column to datetime & gets year/month as features.

    Keyword arguments:
    df -- the dataframe to preprocess
    """
    # Eliminate Whitespaces in columns & Date time the date column
    df = preprocess_data_input(df)
    df["year"] = df["date"].dt.year
    df["month"] = df["date"].dt.month

    return df


@st.cache_data(show_spinner=False)
def load_data_from_google_drive(file_to_load: str):
    """
    Load data from Google Drive into a DataFrame
    :param file_to_load: The ID of the file to load from Google Drive
    :return: A DataFrame containing the data from the file
    """

    # Define the scope for accessing Google Drive - Read Only
    SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

    # Create API client
    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["google_cloud"], scopes=SCOPES
    )

    # Create a Google Drive API service object
    drive_service = build("drive", "v3", credentials=credentials)

    request = drive_service.files().get_media(fileId=file_to_load)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        fh.seek(0)  # Reset the file pointer to the beginning
        if fh.readable():
            return fh


@st.cache_data(show_spinner=False)
def dataframe_reader(
    file_path: Path, use_columns: Optional[List[str]] = None, reset_index=False, *kwargs
) -> pd.DataFrame:
    """
    Read data from various file formats and return a DataFrame.

    Parameters:
        file_path (Path): The path to the input file.
        use_columns (Optional[List[str]]): A list of column names to include in the DataFrame.
                                           If None, all columns will be included.
                                           Default is None.
        reset_index (bool): Flag if want to reset index from original file.
        *kwargs (Optional[List]): Any keyword arguments to be passed to pandas reader function

    Returns:
        pd.DataFrame: A DataFrame containing the data from the input file.

    Raises:
        ValueError: If the file type is not supported.

    Note:
        Supported file formats: '.csv', '.sav', '.dta', '.pickle'.
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)

    if file_path.suffix == ".csv":
        data = pd.read_csv(file_path, usecols=use_columns, *kwargs)
    elif file_path.suffix == ".sav":
        data = pd.read_spss(file_path, usecols=use_columns, *kwargs)
    elif file_path.suffix == ".dta":
        data = pd.read_stata(file_path, columns=use_columns, *kwargs)
    elif file_path.suffix == ".parquet":
        data = pd.read_parquet(file_path, columns=use_columns, *kwargs)
    elif (file_path.suffix == ".pickle") or (file_path.suffix == ".pkl"):
        data = pd.read_pickle(file_path, *kwargs)
        if use_columns is not None:
            data = data[use_columns]
    else:
        raise ValueError("File type not supported.")

    if reset_index:
        data = data.reset_index()
    return data

def check_memory_and_disk_usage():
    gb_size = 1024 * 1024 * 1000
    used_memory = psutil.virtual_memory().used
    calculated_used_memory = psutil.virtual_memory().total - psutil.virtual_memory().available
    print(f"The 'used' memory: {used_memory / gb_size}")
    print(f"The caculated used memory: {calculated_used_memory / gb_size}")
    # print(f"The used swap memory: {psutil.swap_memory().percent}")
    # print(f"The used disk space: {psutil.disk_usage('/').percent}")
