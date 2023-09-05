from src.weather.weather_pipeline import combine_map_weather
from src.weather.source_weather_data import get_weather_data
from src.weather.constants import (
    RAW_PATH_INTERPOLATED_PRECIPITATION,
    RAW_PATH_INTERPOLATED_TEMPERATURE,
    NIGERIA_SHAPE_PATH_FILE,
    SPI_PATH_FILE,
    GEO_COLUMNS,
)


def run_pipeline(
    source_weather_data: bool == False,
):
    weather_data_name = (
        "temperature"  # we should create drop menu for this in the dashboard
    )
    target_epsg = 4326  # we should create drop menu for this in the dashboard
    col_dissolve = "admin1Pcod"  # we should create drop menu for this in the dashboard
    level = "season"  # we should create drop menu for this in the dashboard
    if level == "daily":
        agg_dict = {weather_data_name: "mean"}
        level = weather_data_name
    else:
        agg_dict = {
            "mean": "mean",
            "min": "mean",
            "max": "mean",
        }
    # get weather data
    (
        nigeria_shape_df,
        weather_temperature_df,
        weather_precipitation_df,
    ) = get_weather_data(
        spi_path=SPI_PATH_FILE,
        source_weather_data=source_weather_data,
        nigeria_shape_path=NIGERIA_SHAPE_PATH_FILE,
        data_path_precipitation=RAW_PATH_INTERPOLATED_PRECIPITATION,
        data_path_temperature=RAW_PATH_INTERPOLATED_TEMPERATURE,
        GEO_COLUMNS=GEO_COLUMNS,
    )

    combined_weather_map = combine_map_weather(
        nigeria_shape_df=nigeria_shape_df,
        weather_precipitation_df=weather_precipitation_df,
        weather_temperature_df=weather_temperature_df,
        col_dissolve=col_dissolve,
        weather_data_name=weather_data_name,
        agg_dict=agg_dict,
        level=level,
        target_epsg=target_epsg,
    )


if __name__ == "__main__":
    run_pipeline(source_weather_data=False)
