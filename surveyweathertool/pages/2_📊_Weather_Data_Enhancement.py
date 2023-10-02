# Page for Weather Data Tool

import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np
import time

# from meteostat import Point, Stations, Daily, Monthly
from datetime import datetime, date, timedelta
from src.dashboard.utils import read_logos
from src.dashboard.utils import (
    check_if_df_has_lat_long,
    preprocess_data_input,
    preprocess_weather_data,
    load_data_from_google_drive
)
from src.weather_x_survey.weather_survey import merge_weather_household

from src.weather.constants import (
    PRECIPITATION_FILE,
    TEMPERATURE_FILE,
    JOINED_WEATHER_DATA_FILE,
    TEMPERATURE_INDICATORS,
    PRECIPITATION_INDICATORS,
)
from src.dashboard.utils import parse_command_arguments

# Parse the arguments passend when running the streamlit run command
datalocation, computation = parse_command_arguments()

# Page Configuration
st.set_page_config(page_title="Weather Data Enhancement", page_icon="📊")

# Page Aesthetics and Text
st.markdown("# Weather Data Enhancement")
st.sidebar.header("Weather Data Add-on")

st.markdown("## Procedure")
st.write(
    """    After you upload a dataset consisting of geographic information, we will attach weather columns 
                detailing some weather information about the geo-coordinates you've uploaded and return the file back to you
                The raw weather data is collected [here](https://psl.noaa.gov/data/gridded/index.html)"""
)
st.write(
    """ Currently, our data only suffices for Nigeria during the years of 1992-2022"""
)

st.markdown("## Requirements")
st.markdown(
    """For this tool to run properly, please make sure to have the following 
             requirements in your dataset: """
)
st.markdown('- Column titled "lat" indicating the latitude of a certain point')
st.markdown('- Column titled "lon" indicating the longitude of a certain point')
st.markdown('- Column titled "date" indicating the date of a certain point')

# Add Sidebar image and Text
STCimage, UNICEFimage, DSAimage, NOAAimage = read_logos("surveyweathertool/logos")
st.sidebar.image(NOAAimage, width=150)
st.sidebar.markdown(
    """The Temperature and Precipitation we use comes from the 
                    National Oceanic and Atmospheric Admnistration (NOAA) Climate Prediction Center"""
)


# Add file upload element
uploaded_file = st.file_uploader("Choose a file to add weather columns", type="csv")


# Run the following code only if a file is uploaded
if uploaded_file is not None:
    st.toast("Input data is being read and preprocessed", icon="⌛")
    start_time = time.time()
    # Read the file
    input = pd.read_csv(uploaded_file)
    # Display the top 5 rows of the file
    st.write("This is the uploaded input data:")
    st.write(input.head(5))
    # Preprocess the input data
    input = preprocess_data_input(input)
    # Error checks file
    check_if_df_has_lat_long(input)

    # Read Weather data (Temp and Precip with climate columns) and preprocess it
    st.toast("Weather data is being read and preprocessed", icon="⌛")
    with st.spinner("Weather data is being read and preprocessed..."):
        # Defining all indicators to aggregate and return attached to uploaded data
        weather_data_indicators_dict = {
            "precipitation": ["precipitation", "heavy_rain_index", "spi_index"],
            "temperature": ["temperature", "heatwave_index"],
        }
        merged_data = input.copy()

        if datalocation == "gdrive" and computation == "low_resource":
            weather_data = load_data_from_google_drive(
                file_to_load=JOINED_WEATHER_DATA_FILE
            )
            weather_data_df = pd.read_parquet(weather_data)
            weather_data_df = preprocess_weather_data(weather_data_df)

        elif datalocation == "gdrive" and computation == "high_resource":
            precipitation_indicators_data = load_data_from_google_drive(
                file_to_load=PRECIPITATION_FILE
            )
            precipitation_indicators = pd.read_parquet(precipitation_indicators_data)
            precipitation_indicators = preprocess_weather_data(precipitation_indicators)
            temperature_indicators_data = load_data_from_google_drive(
                file_to_load=TEMPERATURE_FILE
            )
            temperature_indicators = pd.read_parquet(temperature_indicators_data)
            temperature_indicators = preprocess_weather_data(temperature_indicators)

        elif datalocation == "local" and computation == "high_resource":
            precipitation_indicators = pd.read_parquet(PRECIPITATION_INDICATORS)
            precipitation_indicators = preprocess_weather_data(precipitation_indicators)
            temperature_indicators = pd.read_parquet(TEMPERATURE_INDICATORS)
            temperature_indicators = preprocess_weather_data(temperature_indicators)

    st.toast("Weather features are being created", icon="⌛")
    # Iterate over each column
    with st.spinner("Weather features are being created..."):
        for key, value_cols in weather_data_indicators_dict.items():
            if computation == "high_resource":
                if key == "precipitation":
                    weather_df = precipitation_indicators
                elif key == "temperature":
                    weather_df = temperature_indicators
            else:
                if key == "precipitation":
                    weather_df = weather_data_df
                elif key == "temperature":
                    weather_df = weather_data_df
            for indicator in value_cols:
                # Retrieve weather information for the input using interpolated weather data
                merged_weather_data = merge_weather_household(
                    input, weather_df, indicator
                )
                merged_data = pd.merge(
                    merged_data,
                    merged_weather_data,
                    how="left",
                    on=["lat", "lon", "date"],
                )

    st.toast("Weather features have been successfully created", icon="⌛")
    # Print out new dataset and get it download-ready
    st.write("This is the input data enriched with weather features:")
    st.write(merged_data.head(10))
    print(f"--- Total seconds needed --- {round(time.time() - start_time, 2)}")
    # Return the malleated data to the user
    st.download_button(
        label="Download Weather-Enhanced Data",
        data=merged_data.to_csv(index=False).encode("utf-8"),
        file_name="new_data.csv",
        mime="text/csv",
    )


# Side Bar Set Up
st.sidebar.markdown(
    """
        <style>
            [data-testid="stVerticalBlock"] > img:first-child {
                margin-top: -60px;
            }

            [data-testid=stImage]{
                text-align: center;
                display: block;
                margin-left: auto;
                margin-right: auto;
                width: 100%;
            }
        </style>
        """,
    unsafe_allow_html=True,
)

# Adding the "About the App" Infomration at the bottom of the Page
with st.sidebar.expander("About the App"):
    st.write(
        """
                This project, in collaboration with the Data Science for Social Good (DSSG 2023) organization, 
                the United Nation's Child Emergency Fund (UNICEF), and Save the Children (STC), was made by 
                team JMPST as a way to combat cross-visualization challenges between extreme weather events and 
                child poverty.
                """
    )

st.sidebar.markdown(
    f"<h5 style='text-align: center; color: black;'>Copyright (c) 2023 Data Science for Social Good (RPTU and DFKI) </h4>",
    unsafe_allow_html=True,
)