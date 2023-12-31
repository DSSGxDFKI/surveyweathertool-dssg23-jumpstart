from pathlib import Path

RAW_DATA_PATH = Path("/app/data/raw")
PATH_DASHBOARD_INPUT_DATA = "surveyweathertool/data"
NIGERIA_SHAPE_PATH_FILE = (
    f"{PATH_DASHBOARD_INPUT_DATA}/nga_admin/nga_admbnda_adm2_osgof_20170222.shp"
)

LOGOS_PATH = "surveyweathertool/logos"
PROCESSED_DATA_PATH = Path("/app/data/processed")
PROCESSED_WEATHER_PATH = Path(f"{PROCESSED_DATA_PATH}/weather")

PROCESSED_INTERPOLATED_DATA_PATH = Path(
    f"{PROCESSED_WEATHER_PATH}/interpolated_weather"
)
RAW_PRECIPITATION_PATH = (
    f"{PROCESSED_WEATHER_PATH}/nasa_historical_precipitation/final_precipitation.pickle"
)
RAW_TEMPERATURE_PATH = (
    f"{PROCESSED_WEATHER_PATH}/era5_temperature/final_temperature.pickle"
)
GEO_COLUMNS = ["lon", "lat"]

RAW_PATH_INTERPOLATED_TEMPERATURE = (
    f"{PROCESSED_WEATHER_PATH}/era5_temperature/final_temperature_interpolated.pickle"
)
RAW_PATH_NIG_CLIPPED_PRECIPITATION = f"{PROCESSED_WEATHER_PATH}/nasa_historical_precipitation/final_clipped_precipitation.pickle"

PRECIPITATION_INDICATORS = (
    f"{PROCESSED_WEATHER_PATH}/interpolated_weather/all_precipitation_indicators.pickle"
)
TEMPERATURE_INDICATORS = f"{PROCESSED_WEATHER_PATH}/interpolated_weather/all_temperature_interpolated_indicators.pickle"
SPI_PATH_FILE = PRECIPITATION_INDICATORS

# Dasbhoard input data on Google Drive
LSMS_SURVEY_FILE = "16K6TFFe9nZD_tos5YDBrEVWHAA4zNx4P"
JOINED_WEATHER_DATA_FILE = "1WLaf5ywBGJLhpr8VvLr67VRK3tL_KQSN"

# THESE ARE THE VERY FINE-GRANULAR WEATHER FILES -> CAN NOT BE USED WITH STREAMLIT CLOUD DUE TO OOM ISSUES
PRECIPITATION_FILE = "1L4htbJs3spx-Ojy2sRz82YAmO4nKBkc1"
TEMPERATURE_FILE = "1_6PtYtEbneuSeq4wywQDvKbrpOqZpOvt"

