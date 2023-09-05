from pathlib import Path
import pandas as pd

# TODO: 1) unit tests, 2) remove hardcoding and col_names, rename etc, 3) modularise further, if possible


def get_geo_weather_wave(filepath: Path) -> pd.DataFrame:
    """
    Processing of geo data for each of the four nigerian waves.

    Parameters
    -------
    filepath (Path): Pathlib Path to Geo+weather data wave file in .dta (STATA) format

    Returns
    -------
    pandas.DataFrame: with selected indicator columns including latitude, longitude, and select temperature and precipitation info

    Notes
    -------
    LSMS-ISA survey files have small inconsistencies in naming scheme (column name) even in harmonised datasets!
    So this function renames similar questions with different labels into a single label,
    so that the data across the waves can be concatenated nicely.

    Extensions
    -------
    Function can easily be extended for additional columns from the geo data files.
    If column name is same across the waves, add it to the 'cols' list, and optionally rename in 'rename_cols'
    If column name is unique, then add it into the if-else ladder for each particular file.
    If there is new wave in future, eg Wave 5, add another if statement for unique name columns.
    """

    # Create ifelse ladder for each of the unique columns in files
    # FUTURE TODO: bash script prior to pipeline which harmonises all the column names to same !
    if filepath.parts[-1] == "nga_householdgeovars_y4.dta":
        wave = 4
        unique_cols = ["twi", "h2018_tot", "lat_dd_mod", "lon_dd_mod"]
        unique_renaming_dict = {
            "twi": "potential_wetness_index",
            "h2018_tot": "rainfall_total_in_wave_year",
            "lat_dd_mod": "latitude",
            "lon_dd_mod": "longitude",
        }
    elif filepath.parts[-1] == "NGA_HouseholdGeovars_Y3.dta":
        wave = 3
        unique_cols = ["twi_nga", "h2015_tot", "LAT_DD_MOD", "LON_DD_MOD", "distY1Y3"]
        unique_renaming_dict = {
            "twi_nga": "potential_wetness_index",
            "h2015_tot": "rainfall_total_in_wave_year",
            "LAT_DD_MOD": "latitude",
            "LON_DD_MOD": "longitude",
            "distY1Y3": "distance_bw_householdloc_from_w1",
        }
    elif filepath.parts[-1] == "NGA_HouseholdGeovars_Y2.dta":
        wave = 2
        unique_cols = ["twi_nga", "h2012_tot", "LAT_DD_MOD", "LON_DD_MOD", "distY1Y2"]
        unique_renaming_dict = {
            "twi_nga": "potential_wetness_index",
            "h2012_tot": "rainfall_total_in_wave_year",
            "LAT_DD_MOD": "latitude",
            "LON_DD_MOD": "longitude",
            "distY1Y2": "distance_bw_householdloc_from_w1",
        }
    elif filepath.parts[-1] == "NGA_HouseholdGeovariables_Y1.dta":
        wave = 1
        unique_cols = ["twi_nga", "h2010_tot", "lat_dd_mod", "lon_dd_mod"]
        unique_renaming_dict = {
            "twi_nga": "potential_wetness_index",
            "h2010_tot": "rainfall_total_in_wave_year",
            "lat_dd_mod": "latitude",
            "lon_dd_mod": "longitude",
        }
    # Selected column names which are consistenly named correctly accross all four waves
    cols = [
        "hhid",
        "af_bio_1",
        "af_bio_8",
        "af_bio_12",
        "af_bio_13",
        "af_bio_16",
        "anntot_avg",
        "wetQ_avg",
    ] + unique_cols
    rename_cols = {
        "af_bio_1": "mean_temp_annual",
        "af_bio_8": "mean_temp_wettest_month",
        "af_bio_12": "precip_annual",
        "af_bio_13": "precip_wettest_month",
        "af_bio_16": "precip_wettest_quarter",
        "anntot_avg": "rainfall_avg_annual",
        "wetQ_avg": "rainfall_avg_total_in_wettest_month",
    }
    rename_cols.update(unique_renaming_dict)

    print("Reading: ", filepath.parts[-1])
    geo_wv = pd.read_stata(filepath, columns=cols)  # Read the data

    # Add wave information
    wave_col_name = "wave"
    geo_wv[wave_col_name] = wave
    geo_wv[wave_col_name] = geo_wv[wave_col_name].astype(
        "int8"
    )  # Downcast to optimised dtype

    # Set dataframe index on the primary key of this data
    geo_wv = geo_wv.set_index(["hhid", "wave"])
    geo_wv = geo_wv.rename(columns=rename_cols)  # Rename to nice columns

    return geo_wv


def execute_geo_wv(wavepaths: list[Path], export_name: Path):
    """
    Master execution function for processing geographic and weather information from survey waves

    Parameters
    wavepath (Path) : List of Path to all geo data files from LSMS-ISA indivual survey files
    """

    # Starting message
    print("\nProcessing each waves' geodata file")

    # Running the processing function for each of the geo files, and then concatenating vertically
    # Merging all datasets to create a dataframe with geo information for all the waves
    df = pd.concat([get_geo_weather_wave(wave) for wave in wavepaths])

    # Reorder columns in order of priority/importance
    reorder_cols = [
        "latitude",
        "longitude",
        "potential_wetness_index",
        "mean_temp_annual",
        "mean_temp_wettest_month",
        "precip_annual",
        "precip_wettest_month",
        "precip_wettest_quarter",
        "rainfall_avg_annual",
        "rainfall_avg_total_in_wettest_month",
        "rainfall_total_in_wave_year",
        "distance_bw_householdloc_from_w1",
    ]
    df = df[reorder_cols]

    # Print some summary information about the data
    # Note: Primary key is on 'hhid' and 'wave'. Geo information was only recorded once during the wave
    # print(
    #     'Sucessfully processed and concatenated all waves together with Index as ["hhid","wave"]')
    # print(f"Shape of geo data file is {df.shape}\n",
    #       f"Columns include: {list(df.columns)}")

    return df
