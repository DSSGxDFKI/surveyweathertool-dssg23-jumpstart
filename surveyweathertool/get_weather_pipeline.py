from src.weather.source_weather_data import get_weather_data
from src.weather.constants import (
    RAW_PRECIPITATION_PATH,
    RAW_TEMPERATURE_PATH,
    NIGERIA_SHAPE_PATH_FILE,
    SPI_PATH_FILE,
    GEO_COLUMNS,
)


def run_pipeline(
    source_weather_data: bool == False,
):
    (
        nigeria_shape_df,
        weather_temperature_df,
        weather_precipitation_df,
    ) = get_weather_data(
        spi_path=SPI_PATH_FILE,
        source_weather_data=source_weather_data,
        nigeria_shape_path=NIGERIA_SHAPE_PATH_FILE,
        data_path_precipitation=RAW_PRECIPITATION_PATH,
        data_path_temperature=RAW_TEMPERATURE_PATH,
        GEO_COLUMNS=GEO_COLUMNS,
    )


if __name__ == "__main__":
    run_pipeline(source_weather_data=False)