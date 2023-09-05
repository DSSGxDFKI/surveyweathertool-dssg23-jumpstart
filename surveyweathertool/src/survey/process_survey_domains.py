from typing import List, Dict
import pathlib
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import numpy as np
import os
from src.survey.aggregate_time_waves import *
from src.survey.aggregate_geo_waves import *
from src.survey.get_survey_data import *
from src.survey.balanced_dataset_poverty_indicators import *
from src.survey.constants import *
from src.survey.helper import *

def get_domain(domain: str, import_root_dir="/app/data/raw/survey/nigeria/NGA_2010-2019_NUPD_v01_M_Stata/"
               ):
    '''
    Generalised and modularised function to process all the sub domains of survey

    Guaranteed works for Nigeria STATA survey data, may need to be tweaked to work for other countries
    '''

    # Create absolute filepaths to all files located in survey root directory
    survey_filepaths = {filename: os.path.join(import_root_dir, filename)
                        for filename in os.listdir(import_root_dir)}

    # Create mappings to files and functions for each domain
    roster = 'roster'
    education = 'education'
    housing = 'housing'
    health = 'health'
    nutrition = 'nutrition'

    domain_file_mapping = {
        roster:   ['nup_pp_mod_a_b.dta', 'nup_phx_mod_flap_a_roster_b.dta'],
        education:   ['nup_pp_mod_c.dta', 'nup_ph_mod_c.dta'],
        health:   ['nup_phx_mod_e.dta', 'nup_phx_mod_d.dta'],
        housing:   ['nup_pp_mod_v.dta', 'nup_ph_mod_v.dta'],
        nutrition:   ['nup_pp_mod_s.dta', 'nup_ph_mod_s.dta'],
    }
    domain_processing_fn_mapping = {
        roster:   get_roster_df,
        education:   get_education_df,
        health:   get_health_df,
        housing:   get_housing_df,
        nutrition:   get_nutrition_df,

    }

    # Select domain and processing functions based on given input
    if domain not in domain_file_mapping.keys():
        raise ValueError('Specified domain is out of scope')
    else:
        filenames = domain_file_mapping[domain]
        processing_fn = domain_processing_fn_mapping[domain]
        # Get full filepaths to file location
        filepaths = [survey_filepaths[file] for file in filenames]

    # Run processing function for each file
    print(f'Processing {domain} survey files')
    domain_df_list = []
    for filepath in filepaths:
        domain_df_list.append(processing_fn(filepath))

    ####################
    # NOTE:
    # Health files for post-planting and post-harvest should be concatenated with axis=1, instead of axis=0,
    # otherwise they introduce duplicates values

    # Concatenate the files together, and sort by pandas index
    if domain == health:
        # 1.08.23 Health duplication hotfix
        domain_df = pd.concat(domain_df_list, axis=1)
    else:
        domain_df = pd.concat(domain_df_list, axis=0)

    # Sort by index
    domain_df = domain_df.sort_index()

    print(f'DONE! Processing {domain} survey files succesfully completed!')

    return domain_df


def process_survey_domains(import_root_dir="/app/data/raw/survey/nigeria/NGA_2010-2019_NUPD_v01_M_Stata/",
                           export_root_dir="/app/data/processed/survey",
                           export_flag=True,
                           export_format='.csv',
                           ):
    '''
    Creates raw subdomain level files from downloaded raw survey data
    '''
    print("Hello. This is the entrypoint into survey processing")
    ####################################################################################
    # Process each domain level dataset
    roster = 'roster'
    education = 'education'
    housing = 'housing'
    health = 'health'
    nutrition = 'nutrition'
    domain_list = [roster, housing, education, health, nutrition]

    # domain_df_list = []
    for domain in domain_list:
        domain_df = get_domain(domain)
        # Make all indices common for later usage
        domain_df = create_common_index(domain_df)

        # If exporting required
        if export_flag:
            export_fn(domain_df, f'{export_root_dir}/{domain}', export_format)
        # Append into data structure
        # domain_df_list.append(domain_df)

    ####################################################################################
    # Get Geographic information about households from each individual wave
    geo_export_name = 'geo'
    geo = execute_geo_wv(wavepaths=SURVEY_GEOLOCATION_DATA_PATH,
                         export_name=EXPORT_GEO_DATA_FILENAME)

    if export_flag:
        export_fn(geo, f'{export_root_dir}/{geo_export_name}', export_format)

    #############################################################################
    # Get day of survey from individual wave files

    day_of_survey_export_name = 'day_of_survey'
    day_of_survey = get_survey_timestamps(DATATIME_DATA_NIGERIA_WAVES_DICT)

    if export_flag:
        export_fn(
            day_of_survey, f'{export_root_dir}/{day_of_survey_export_name}', export_format)

    #############################################################################
    # Ending message
    print('\nProcessed raw survey data into domain level files')
    return