from typing import Dict, List
import pandas as pd
import numpy as np

def get_wave_timestamp(file_path_dict: Dict[str, Dict[str, str]], wave_type: str, use_columns: List[str]) -> pd.DataFrame:
    """
    Read data files for a specific wave, merge them, and process timestamps.

    Parameters:
        file_path_dict (Dict[str, Dict[str, str]]): A dictionary containing file paths for different waves.
        wave (str): The wave to process.
        use_columns (List[str]): The list of columns to use from the data files.

    Returns:
        pd.DataFrame: The merged and processed DataFrame with timestamps.
    """
    
    def _wave_timestamp_imputer(df: pd.DataFrame):
        """
        Impute missing values in the 'day', 'month', and 'year' columns of a DataFrame using random values.

        This function replaces NaN values in each column with random values generated from the unique non-NaN
        values of that column. It specifically handles the 'day', 'month', and 'year' columns.

        Parameters:
            df (pd.DataFrame): The DataFrame containing the columns to be imputed.

        Returns:
            None. The input DataFrame is modified in place with the imputed values.
        """
        for col in ["day", "month", "year"]:
            if col == "month":
                df[col] = df[col].astype(str).str.extract(r'(\d+)').astype(float)

            if df[col].isna().any():
                non_nan_values = sorted(df[col].dropna().unique())
                sample_size = df[col].isna().sum()

                # Calculate the min and median of the non-NaN values
                min_value = np.min(non_nan_values)
                median_value = np.median(non_nan_values)

                # Create an array of random integer choices between min and median
                random_values = np.random.choice(np.arange(min_value, median_value + 1), size=sample_size)

                nan_indices = df[col].isna()
                df.loc[nan_indices, col] = random_values
                df[col] = df[col].astype("int").astype("str")
                    
        # Combine 'day', 'month', and 'year' columns to form 'date' column
        df['date'] = pd.to_datetime(df['day'] + '-' + df['month'] + '-' + df['year'], format="%d-%m-%Y", errors='coerce')

        # Handle cases where the date is invalid (NaT) by subtracting 2 from the day [Feb and Sept]
        invalid_date = df['date'].isna()
        df.loc[invalid_date, 'date'] = pd.to_datetime(
            (df.loc[invalid_date, 'day'].astype(int) - 2).astype(str) + '-' + df.loc[invalid_date, 'month'] + '-' +
            df.loc[invalid_date, 'year'],
            format="%d-%m-%Y", errors='coerce'
        )

            
    visits = []
    
    for key, value in {"planting": "Post-Planting", "harvest": "Post-Harvest"}.items():
        wave_path = file_path_dict[wave_type]
        df = pd.read_stata(f"{wave_path['path']}{wave_path[key]}", columns=use_columns) # Doesnt work with Wave 4?? 
        df["visit"] = value
        df["wave"] = wave_type
        visits.append(df)

    wave = pd.concat(visits)
    rename_columns = {"saq13d": "day", "saq13m": "month", "saq13y": "year"}
    wave.rename(columns=rename_columns, inplace=True)
    
    wave["wave"] = pd.to_numeric(wave['wave'], downcast="integer")
    wave["visit"] = wave.visit.astype("category")
    
    # Replace NaN values in each column with random values from the unique values of that 
    _wave_timestamp_imputer(wave)

    # Drop the 'day', 'month', and 'year' columns
    wave.drop(['day', 'month', 'year'], axis=1, inplace=True)
    return wave

def get_survey_timestamps(datetime_dict):
    '''
    Master processing function that return combined dataframe with survey timestamps at individual level
    '''
    print('Processing day of survey timestamp from each waves\' files')
    timestamp_columns = ["hhid", "saq13d", "saq13m","saq13y"]

    desired_waves = ['1', '2', '3'] # If more or less waves needed specify here
    waves_timestamp_list = []
    for wave in desired_waves:
        waves_timestamp_list.append(get_wave_timestamp(datetime_dict, wave, timestamp_columns))

    # Concatenate all the desired wave level information into one
    waves_timestamp = pd.concat(waves_timestamp_list)

    ## To merge together with other survey domains, change dtype of visit, and add index
    visit = 'visit'
    index_cols = ['hhid','wave', 'visit']

    waves_timestamp[visit] = np.where(waves_timestamp[visit] == 'Post-Planting', 1, 2)
    waves_timestamp[visit] = waves_timestamp[visit].astype('int')

    waves_timestamp = waves_timestamp.set_index(index_cols) # set index

    print('DONE! Processing day of survey timestamp from each waves\' files completed')

    return waves_timestamp