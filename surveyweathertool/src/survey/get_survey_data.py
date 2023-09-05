import pandas as pd
import re  # Regex in python
import numpy as np


def create_common_index(df: pd.DataFrame) -> pd.DataFrame:
    """

    Function which harmonises the different survey df indices

    """
    hhid = "hhid"
    indiv = "indiv"
    wave = "wave"
    visit = "visit"
    index_cols = [hhid, wave]
    int_dtype = "int"
    df = df.reset_index()

    df[hhid] = df[hhid].astype(int_dtype)
    df[wave] = np.where(
        df[wave] == "1. Wave 1-2010/11",
        1,
        np.where(
            df[wave] == "2. Wave 2-2012/13",
            2,
            np.where(
                df[wave] == "3. Wave 3-2015/16",
                3,
                np.where(df[wave] == "4. Wave 4-2018/19", 4, 0),
            ),
        ),
    )
    df[wave] = df[wave].astype(int_dtype)

    if visit in df.columns:
        PP_VISIT_OPTIONS = ["1. Post-Planting"]
        PH_VISIT_OPTIONS = ["Post-Harvest", "2. Post-Harvest"]

        df[visit] = np.where(
            df[visit].isin(PP_VISIT_OPTIONS),
            1,
            np.where(df[visit].isin(PH_VISIT_OPTIONS), 2, 0),
        )
        df[visit] = df[visit].astype(int_dtype)
        index_cols.insert(len(index_cols), visit)

    if indiv in df.columns:
        df[indiv] = df[indiv].astype(int_dtype)
        index_cols.insert(1, indiv)  # indiv is second after hhid

    # Set index again
    df = df.set_index(index_cols)

    return df


def get_roster_df(cover_filepath) -> pd.DataFrame:
    """Given flap file returns hhid, indiv id location, age, sex and temporal info for all individuals who ever answered a survey"""
    flap_file = pd.read_stata(cover_filepath)
    primary_key_cols = ["hhid", "indiv"]
    location_cols = ["ea", "lga", "sector", "state", "zone"]
    temporal_cols = ["wave", "visit"]
    hh_head_cols = ["ha_06"]
    sex_cols = ["ha_05"]
    some_housing_cols = []

    # NOTE: In both of the cover files, age has different label names!!
    # its 'ha_07' in post harvest, but 'ha_08' in post planting !!
    if re.search(r"flap", cover_filepath):
        # Very few have DOB information ['ha_12_day', 'ha_12_month', 'ha_12_year']
        age_cols = ["ha_07"]
        rename_dict = {
            "ha_05": "sex",
            "ha_06": "relationship_to_hh_head",
            "ha_07": "age",
        }
    else:
        # Very few have DOB information ['ha_12_day', 'ha_12_month', 'ha_12_year']
        age_cols = ["ha_08"]
        rename_dict = {
            "ha_05": "sex",
            "ha_06": "relationship_to_hh_head",
            "ha_08": "age",
        }

    df = flap_file[
        primary_key_cols
        + location_cols
        + temporal_cols
        + hh_head_cols
        + sex_cols
        + age_cols
    ]
    df = df.rename(columns=rename_dict)

    # Add total number of people in household information
    num_people_hh = (
        df.groupby(["hhid", "wave"])["indiv"]
        .agg(["nunique"])
        .rename(columns={"nunique": "num_people_hh"})
    )

    df = df.set_index(primary_key_cols + temporal_cols)
    df = df.join(num_people_hh, how="left")
    resort_cols = [
        "age",
        "sex",
        "relationship_to_hh_head",
        "num_people_hh",
        "ea",
        "lga",
        "sector",
        "state",
        "zone",
    ]
    df = df[resort_cols]

    return df


def get_education_df(filename) -> pd.DataFrame:
    """Get Education columns from LSMS harmonised Nigeria"""
    df = pd.read_stata(filename)

    # Human legible column names
    primary_key_cols = ["hhid", "indiv", "wave", "visit"]
    education_cols = ["hc_06", "hc_07"]
    age_cols = ["hc_03"]

    # NOTE: In both of the cover files, currently in school has different label names!!
    # its 'ha_17' in post harvest, but 'ha_12' in post planting !!
    # if re.search(r'nup_pp_mod_c.dta', filename):
    #     rename_dict = {'hc_03': 'age_5y_older', 'hc_06': 'read_write_language',
    #                     'hc_07': 'ever_attended_school', }
    # else:
    rename_dict = {
        "hc_03": "age_5y_older",
        "hc_06": "read_write_language",
        "hc_07": "ever_attended_school",
    }

    df = df[primary_key_cols + education_cols + age_cols]
    df = df.rename(columns=rename_dict)
    df = df.set_index(primary_key_cols)

    return df


def get_health_df(filename):
    """Get Health columns from LSMS harmonised Nigeria"""

    df = pd.read_stata(filename)
    primary_key_cols = ["hhid", "indiv", "wave", "visit"]

    if re.search(r"nup_phx_mod_e.dta", filename):
        health_cols = ["he_08", "he_10", "he_11", "he_12"]
        rename_dict = {
            "he_08": "measles_immunisation",
            "he_10": "dpt1_immunisation",
            "he_11": "dpt2_immunisation",
            "he_12": "dpt3_immunisation",
        }
    else:
        health_cols = ["hd_09a", "hd_44", "hd_45"]
        rename_dict = {
            "hd_09a": "last_consulted_healthcare_type",
            "hd_44": "family_planning_flag",
            "hd_45": "family_planning_type",
        }

    df = df[primary_key_cols + health_cols]
    df = df.rename(columns=rename_dict)
    df = df.set_index(primary_key_cols)

    return df


def get_housing_df(filepaths):
    """Get Shelter, Sanitation, & Water columns from LSMS harmonised Nigeria"""

    df = pd.read_stata(filepaths)

    # Human legible column names
    primary_key_cols = ["hhid", "wave", "visit"]
    shelt_sanit_wat_cols = ["hv_13", "hv_51", "hv_50", "hv_48a", "hv_48b", "hv_47b"]

    rename_dict = {
        "hv_13": "num_separate_rooms",
        "hv_51": "shared_sanit",
        "hv_50": "sanit_type",
        "hv_48a": "time_to_water",
        "hv_48b": "water_time_unit",
        "hv_47b": "drink_water_source",
    }

    selected_cols = primary_key_cols + shelt_sanit_wat_cols
    df = df[selected_cols]

    df = df.rename(columns=rename_dict)

    df = df.set_index(primary_key_cols)

    return df


def get_nutrition_df(filepaths):
    """
    Get Nutrition columns from LSMS harmonised Nigeria

    nup_pp_mod_s.dta  → hs_05 & hs_01g
    nup_ph_mod_s.dta → hs_05 & hs_01g
    """

    df = pd.read_stata(filepaths)

    # Human legible column names
    primary_key_cols = ["hhid", "wave", "visit"]
    nutrition_cols = ["hs_05", "hs_01g"]

    rename_dict = {"hs_05": "situation_no_food", "hs_01g": "num_days_no_food"}

    selected_cols = primary_key_cols + nutrition_cols
    df = df[selected_cols]

    df = df.rename(columns=rename_dict)

    df = df.set_index(primary_key_cols)

    return df
