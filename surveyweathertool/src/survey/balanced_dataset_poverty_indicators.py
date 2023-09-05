import pandas as pd
import numpy as np
from src.survey.helper import export_fn, dataframe_reader
from typing import List, Dict

def merge_all(roster: pd.DataFrame, df_list: list[pd.DataFrame]) -> pd.DataFrame:
    '''
    Merges all survey dataframes into one.

    METHODOLOGY
    ----------
    Current methodology is to left join all the individual subdomains onto the survey 'roster' file.

    This is because the survey roster contains all the (hhid,indiv,wave,visit) combinations ever recorded in any part of the survey

    '''

    # Left join all subdomains into roster file
    for domain in df_list:
        roster = roster.join(domain, how='left')

    return roster


def balanced_panel_analysis(processed_filepath: str, domains_to_merge: List, data_format: str) -> pd.DataFrame:
    '''
    Not fully completed balanced panel creation for Child <18 and waves 1 & 2 and 3
    '''

    # Start balanced panel analysis
    ROSTER_FILEPATH = f"{processed_filepath}/roster{data_format}"
    DOMAIN_FILEPATHS = [f'{processed_filepath}/{domain}{data_format}'
                        for domain in domains_to_merge]

    # Read in roster file master ground truth about entire survey
    roster = dataframe_reader(ROSTER_FILEPATH)
    # Read in all the subdomains
    domain_df = []
    for domain in DOMAIN_FILEPATHS:
        domain_df.append(dataframe_reader(domain))

    #################################################################################
    # Left join all subdomains into roster file
    # [waves_timestamp, geo_data, merged_education, merged_health, nutrition, merged_housing]
    print(f'Merging {domains_to_merge} onto roster file')
    df = merge_all(roster, domain_df)
    print(f'DONE! Successfully merged {domains_to_merge} onto roster file')

    merged_df = 'merged_df'
    export_fn(df, f'{processed_filepath}/{merged_df}', data_format)
    print(f'Shape of merged df is {df.shape}')
    #################################################################################
    # Create poverty index columns
    balanced_panel, child_poverty_index = create_unicef_poverty_index(df)

    # Export the child poverty added columns with the data
    export_fn(balanced_panel,
              f'{processed_filepath}/balanced_panel', data_format)

    export_fn(child_poverty_index,
              f'{processed_filepath}/child_poverty_index_pivot_table', '.pickle')

    return


def make_health_dimension_columns(df):
    """
    Applies health filters to make a column of a value indicating both whether or not a household/individual is deprived and the severity of this deprivation

    Keyword arguments:
    filepath (Path) - Path to health csv

    NOTES
    ----------
    health_indicator_values = [0,1,2], 0 if no data or not poor. 1 if moderate, 2 if severe
    """

    health_indicator = "health_indicator"
    age_col = "age"

    measles = "measles_immunisation"
    dpt1 = "dpt1_immunisation"
    dpt2 = "dpt2_immunisation"
    dpt3 = "dpt3_immunisation"
    yes = "1. YES"
    no = "2. NO"
    family_planning_flag = "family_planning_flag"
    family_planning_type = "family_planning_type"
    traditional_methods = [
        "12. TRADITIONAL METHOD",
        "13. ABSTINENCE",
        "14. WITHDRAWAL",
        "15. RYTHM",
    ]

    # Fix encoding issue
    last_consulted_healthcare_type = "last_consulted_healthcare_type"
    last_consulted_healthcare_type_severe = ["9. TBA", "12. NO ONE(âº)"]
    last_consulted_healthcare_type_not_moderate = [
        "2. DOCTOR",
        "4. NURSE",
        "5. MEDICAL ASST",
        "7. PHARMACIST",
        "11. PATENT MEDICINE VENDOR (PMV)",
        "13. JCHEW",
        "14. CHEW",
    ]
    # df[last_consulted_healthcare_type] = int(str(df[last_consulted_healthcare_type]).split('.')[0])

    # AGE > 15
    conditions = [(df[age_col] >= 15) & (df[family_planning_flag] == no),
                  (df[age_col] >= 15) & (
                      df[family_planning_type].isin(traditional_methods)),
                  (df[family_planning_flag].isna() == True) | (
                      df[family_planning_type].isna() == True)
                  ]
    choices = [2, 1, pd.NA]
    df[health_indicator] = np.select(conditions, choices, default=0)

    # AGES 5-14
    conditions = [(df[age_col] > 5) & (df[age_col] <= 14)]
    choices = [pd.NA]
    df[health_indicator] = np.select(conditions, choices, default=0)

    # AGES 3-5
    conditions = [(df[age_col] >= 3) & (df[age_col] <= 5) & (df[last_consulted_healthcare_type].isin(last_consulted_healthcare_type_severe)),
                  (df[age_col] >= 3) & (df[age_col] <= 5) & ~(
                      df[family_planning_type].isin(last_consulted_healthcare_type_not_moderate)),
                  (df[family_planning_type].isna() == True) | (df[last_consulted_healthcare_type].isna() == True)]
    choices = [2, 1, pd.NA]
    df[health_indicator] = np.select(conditions, choices, default=0)

    # AGES <3
    conditions = [(df[age_col] < 3) & (df[measles] == no) & (df[dpt1] == no) & (df[dpt2] == no) & (df[dpt3] == no),
                  (df[age_col] < 3) & (df[measles] == no) | (
                      df[dpt1] == no) | (df[dpt2] == no) | (df[dpt3] == no),
                  (df[measles].isna() == True) | (df[dpt1].isna() == True) | (df[dpt2].isna() == True) | (df[dpt3].isna() == True)]
    choices = [2, 1, pd.NA]
    df[health_indicator] = np.select(conditions, choices, default=0)

    return df


def make_housing_dimension_columns(df):
    """
    Applies shelter, sanitation, and water filters to make a column of a value indicating both whether or not a household/individual is deprived and the severity of this deprivation

    Keyword arguments:
    filepath (Path) - Path to health csv

    NOTES
    ----------
    shelter_indicator_values = [0,1,2], 0 if no data or not poor. 1 if moderate, 2 if severe
    sanitation_indicator_values = [0,1,2], 0 if no data or not poor. 1 if moderate, 2 if severe
    shelter_indicator_values = [0,1,2], 0 if no data or not poor. 1 if moderate, 2 if severe
    """

    # SHELTER
    shelter_indicator = "shelter_indicator"
    dwelling_ratio = "room_to_indiv_ratio"
    num_separate_rooms = "num_separate_rooms"
    num_people_hh = "num_people_hh"
    df[dwelling_ratio] = df[num_separate_rooms] / df[num_people_hh]

    conditions = [(df[dwelling_ratio] >= 5),
                  (df[dwelling_ratio] >= 3) & (df[dwelling_ratio] < 5),
                  (df[num_separate_rooms].isna() == True) | (df[num_people_hh].isna() == True)]
    choices = [2, 1, pd.NA]
    df[shelter_indicator] = np.select(conditions, choices, default=0)

    # SANITATION
    sanitation_indicator = "sanitation_indicator"
    sanitation_col = "sanit_type"
    severe_sanitation_type = [
        "8. PIT LATRINE W/O SLAB/OPEN PIT",
        "10. BUCKET",
        "11. HANGING TOILET/ HANGING LATRINE",
        "12. NO FACILITIES, BUSH, OR FIELD",
    ]
    shared_sanit = "shared_sanit"
    severe_sanitation_type = ["2. OTHER HOUSEHOLDS ALSO"]

    conditions = [(df[sanitation_col].isin(severe_sanitation_type)),
                  (df[sanitation_col].isin(severe_sanitation_type)),
                  (df[sanitation_col].isna() == True)]
    choices = [2, 1, pd.NA]
    df[sanitation_indicator] = np.select(conditions, choices, default=0)

    # WATER
    drink_water_source, time_to_water, water_time_unit = (
        "drink_water_source",
        "time_to_water",
        "water_time_unit",
    )
    water_indicator = "water_indicator"
    severe_type = [
        "1. PIPED INTO DWELLING",
        "2. PIPED INTO YARD/PLOT",
        "3. PIPED TO NEIGHBOR",
        "4. PUBLIC TAP/STANDPIPE",
        "5. TUBE WELL/BOREHOLE",
        "17. PIPE BORNE WATER TREATED",
    ]

    time_to_water = "time_to_water"
    water_time_unit = "water_time_unit"

    conditions = [~(df[drink_water_source].isin(severe_type)),
                  (df[time_to_water] > 15) | (
                      df[water_time_unit] == '2. HOUR'),
                  (df[time_to_water].isna() == True) | (df[water_time_unit].isna() == True) | (df[drink_water_source].isna() == True)]
    choices = [2, 1, pd.NA]
    df[water_indicator] = np.select(conditions, choices, default=0)

    return df


def make_education_dimension_columns(df):
    # EDUCATION
    education_indicator = "education_indicator"
    age_col = "age"
    ever_attended_school = "ever_attended_school"
    read_write_language = "read_write_language"
    yes = "1. YES"
    no = "2. NO"

    conditions = [(df[age_col] > 5) & (df[ever_attended_school] == no) & (df[read_write_language].isin([no])),
                  (df[age_col] > 5) & (df[ever_attended_school] == no),
                  (df[ever_attended_school].isna() == True) | (
                      df[read_write_language].isna() == True),
                  (df[age_col] <= 5)]
    choices = [2, 1, pd.NA, pd.NA]
    df[education_indicator] = np.select(conditions, choices, default=0)

    return df


def make_nutrition_dimension_columns(df):
    # NUTRITION
    nutrition_indicator = "nutrition_indicator"
    num_days_no_food = "num_days_no_food"
    situation_no_food = "situation_no_food"
    yes = "1. YES"

    conditions = [(df[num_days_no_food] > 1),
                  (df[situation_no_food] == yes),
                  (df[num_days_no_food].isna() == True) | (df[situation_no_food].isna() == True)]
    choices = [2, 1, pd.NA]
    df[nutrition_indicator] = np.select(conditions, choices, default=0)

    return df


def create_unicef_poverty_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    From the combined raw survey data, create the poverty index based on UNICEF definition/conditions.

    REFERENCE
    ---------
    Please see XXXX link for UNICEF definitions
    """

    print(f"Starting from  (rows,cols) : {df.shape}")

    ######### SUBSET TO CHILDREN ONLY #################################################
    # for children only < 18
    age_col = "age"
    df = df[df[age_col] < 18]

    print(f"Dropped age <18. New shape is {df.shape}")

    ######### Drop wave 4 records #################################################
    df = df.drop(index=4, level=1)
    print(f"Dropped wave 4 records now. New shape is {df.shape}")

    ######### Keep only wave 1 & 2 & 3 #################################################

    df_child_indiv = df.reset_index()
    df_child_indiv = df_child_indiv[["hhid", "indiv", "wave"]]

    df_child_indiv = df_child_indiv.groupby(["hhid", "indiv"]).agg(
        num_waves_records=("wave", "count")
    )

    # df_child_indiv["balanced_panel_condition_1"] = np.where(
    #     df_child_indiv["num_waves_records"] >= 5, True, False
    # )
    # df_child_indiv["balanced_panel_condition_2"] = np.where(
    #     df_child_indiv["num_waves_records"] == 6, True, False
    # )

    # print(
    #     f"Out of {df_child_indiv.shape[0]} individual children present over Wave 1-3, only {df_child_indiv['balanced_panel_condition_1'].sum()} individuals have records in all three waves, and only {df_child_indiv['balanced_panel_condition_2'].sum()} individuals have records for both of the visits in all the waves"
    # )

    # Join the balanced condition flag onto main df
    df = df.join(df_child_indiv, how="left")
    # Enforce balanced criterion
    # df = df[df["balanced_panel_condition_2"] == True]

    # print(
    #     f'{df_child_indiv["balanced_panel_condition_2"].sum()} individual children (who have records for all the visits) together have {df.shape[0]} total records. Subsetting to just these records.'
    # )

    ########## Create indicator columns #################################################
    df = make_health_dimension_columns(df)
    df = make_housing_dimension_columns(df)
    df = make_education_dimension_columns(df)
    df = make_nutrition_dimension_columns(df)

    # print(f"Balanced panel (rows,cols) : {df.shape}")

    unicef_poverty_index = "unicef_poverty_index"

    indicators_list = [
        "health_indicator",
        "shelter_indicator",
        "sanitation_indicator",
        "water_indicator",
        "education_indicator",
        "nutrition_indicator",
    ]


    # Apply a lambda function to count non-null values in a row (each indicator column)
    df['non_null_count'] = df.apply(lambda row: row[indicators_list].notna().sum(), axis=1)

    # Calculate the unicef_poverty_index
    df['unicef_poverty_index'] = (df[indicators_list].sum(axis=1) / df['non_null_count']).where(df['non_null_count'] != 0, pd.NA)

    # Create poverty index pivot table with columns for each wave X visit combination
    poverty_index_pivot_table = (df.reset_index()).pivot(
        index=["hhid", "indiv"],
        columns=["wave", "visit"],
        values="unicef_poverty_index",
    )

    return df, poverty_index_pivot_table
