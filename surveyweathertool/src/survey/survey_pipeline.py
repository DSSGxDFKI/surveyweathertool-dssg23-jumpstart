import pandas as pd

from src.survey.process_survey_domains import process_survey_domains
from src.survey.balanced_dataset_poverty_indicators import balanced_panel_analysis
from src.weather_x_survey.weather_survey import merge_survey_weather_hh_level
from src.survey.constants import *


def run_survey_pipeline():
    # Survey prototype pipeline
    NIGERIA_UNIFIED_PANEL_IMPORT_DIR = (
        "/app/data/raw/survey/nigeria/NGA_2010-2019_NUPD_v01_M_Stata/"
    )
    SURVEY_NIGERIA_PROCESSED_DIR = "/app/data/processed/survey/nigeria"
    DATA_FORMAT = ".pickle"  # Choose from {'.pickle', '.csv', 'parquet'}

    # Starting message
    print(
        "Data processing started for: Nigeria General Household Survey 2010-2019 Uniform Panel"
    )
    print(f"Survey data located in: {NIGERIA_UNIFIED_PANEL_IMPORT_DIR}")

    process_survey_domains(
        import_root_dir=NIGERIA_UNIFIED_PANEL_IMPORT_DIR,
        export_root_dir=SURVEY_NIGERIA_PROCESSED_DIR,
        export_flag=True,
        export_format=DATA_FORMAT,
    )

    # Start balanced panel analysis
    # \nPresent in Wave 1 & 2 & 3
    print(
        f"Creating balanced panel based on following conditions:\n\nIndividual level, age<18"
    )
    balanced_panel_analysis(
        SURVEY_NIGERIA_PROCESSED_DIR,
        ["education", "housing", "health", "nutrition", "geo", "day_of_survey"],
        DATA_FORMAT,
    )

    # MERGE SURVEY + WEATHER AT HH LEVEL
    WEATHER_NIGERIA_PROCESSED_HH = (
        "/app/data/processed/survey_weather/household_weather.csv"
    )
    DATA_FORMAT = ".pickle"  # Choose from {'.pickle', '.csv', 'parquet'}
    merge_survey_weather_hh_level(
        f"{SURVEY_NIGERIA_PROCESSED_DIR}/balanced_panel.pickle",
        WEATHER_NIGERIA_PROCESSED_HH,
        export_flag=True,
        export_format=".pickle",
        export_path="/app/data/processed/survey_weather/",
    )

    print("Successful end of survey prototype script")

    return
