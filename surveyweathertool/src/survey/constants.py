# The only file that is 'hardcoded' would need to be changed for the all other survey code to run

# Imports
from pathlib import Path
import os

RAW_DATA_FOLDER_PATH = Path("/app/data/raw/survey/nigeria")
PROCESSED_DATA_FOLDER_PATH = Path("/app/data/processed/survey/nigeria")
SURVEY_FINAL_PATH = Path("/app/data/processed/survey/nigeria/balanced_panel.pickle")

XML_FILE_PATH = f"{RAW_DATA_FOLDER_PATH}/metadata/NGA_2010-2019_NUPD_v01_M.xml"
# TODO: make t uniform
JSON_FILE_PATH = f"{PROCESSED_DATA_FOLDER_PATH}/NGA_2010-2019_NUPD_v01_M.json"
HARMONIZED_DATA_PATH = f"{RAW_DATA_FOLDER_PATH}/NGA_2010-2019_NUPD_v01_M_Stata"
DATA_DICTIONARY_PATH = f"{RAW_DATA_FOLDER_PATH}/data_dictionary.xlsx"
GEOLOCATION_DATA_PATH = f"{RAW_DATA_FOLDER_PATH}/geo.pickle"

FILE_EXTENSION_CHOICES = [".csv", ".dta", ".sav", ".xlsx", ".xls", ".json"]
PRIMARY_COLUMNS = ["wave", "visit", "zone", "state", "lga", "sector", "ea", "hhid"]


# FROM aggregate_geo_waves.py

# Point to the root directory on server
FILEPATH_TO_NIGERIA_DATA = Path("/app/data/raw/survey/nigeria/")

# List of geodata files from each wave
SURVEY_GEOLOCATION_DATA_PATH = [
    FILEPATH_TO_NIGERIA_DATA.joinpath(
        "NGA_2018_GHSP-W4_v03_M_Stata12/nga_householdgeovars_y4.dta"
    ),
    FILEPATH_TO_NIGERIA_DATA.joinpath(
        "NGA_2015_GHSP-W3_v02_M_Stata/NGA_HouseholdGeovars_Y3.dta"
    ),
    FILEPATH_TO_NIGERIA_DATA.joinpath(
        "NGA_2012_GHSP-W2_v02_M_STATA/Geodata Wave 2/NGA_HouseholdGeovars_Y2.dta"
    ),
    FILEPATH_TO_NIGERIA_DATA.joinpath(
        "NGA_2010_GHSP-W1_v03_M_STATA/Geodata/NGA_HouseholdGeovariables_Y1.dta"
    ),
]

# Exporting the outputs into processed data folder
# If export_dir doesnt exist, create it
EXPORT_GEO_DATA = Path("/app/data/processed/survey/nigeria")
# if not EXPORT_GEO_DATA.exists():
#     print('Creating export directory at: {EXPORT_GEO_DATA}')
#     os.makedirs(EXPORT_GEO_DATA)
EXPORT_GEO_DATA_FILENAME = EXPORT_GEO_DATA.joinpath(
    "geo_weather_household_wave_level.csv"
)


# List of datetime files from each wave
DATATIME_DATA_NIGERIA_WAVES_DICT = {
    "1": {
        "path": f"{RAW_DATA_FOLDER_PATH}/NGA_2010_GHSP-W1_v03_M_STATA",
        "planting": "/Post Planting Wave 1/Household/secta_plantingw1.dta",
        "harvest": "/Post Harvest Wave 1/Household/secta_harvestw1.dta",
    },
    "2": {
        "path": f"{RAW_DATA_FOLDER_PATH}/NGA_2012_GHSP-W2_v02_M_STATA",
        "planting": "/Post Planting Wave 2/Household/secta_plantingw2.dta",
        "harvest": "/Post Harvest Wave 2/Household/secta_harvestw2.dta",
    },
    "3": {
        "path": f"{RAW_DATA_FOLDER_PATH}/NGA_2015_GHSP-W3_v02_M_Stata",
        "planting": "/secta_plantingw3.dta",
        "harvest": "/secta_harvestw3.dta",
    },
    "4": {
        "path": f"{RAW_DATA_FOLDER_PATH}/NGA_2018_GHSP-W4_v03_M_Stata12",
    },
}
