import pandas as pd
import json
import streamlit as st
import xmltodict
from pathlib import Path
from typing import Dict, List, Optional
from src.survey.constants import PROCESSED_DATA_FOLDER_PATH


def non_missing_stats(df, list_of_cols) -> pd.DataFrame:
    """Returns non-missing percentages in a dictionary for each column (passed in list) from the df"""
    dictionary = {}
    for col in list_of_cols:
        denom = df.shape[0]
        dictionary.update({col: (denom - df[col].isnull().sum()) / denom})
    return dictionary


def export_fn(df: pd.DataFrame, output_filepath: str, file_extension: str, *kwargs):
    """
    Helper utility for exporting a dataframe to a specific format

    Currently supports '.csv', '.pickle', '.parquet'

    Can pass arguments to the 'to_X' function as kwargs
    """

    # decide function for export
    if file_extension == ".csv":
        func = pd.DataFrame.to_csv
    elif file_extension == ".pickle":
        func = pd.DataFrame.to_pickle
    elif file_extension == ".parquet":
        func = pd.DataFrame.to_parquet

    # Export
    func(df, output_filepath + file_extension, *kwargs)

    print("Successfully exported\n")
    return


def dataframe_reader(
    file_path: Path, use_columns: Optional[List[str]] = None, reset_index=False, *kwargs
) -> pd.DataFrame:
    """
    Read data from various file formats and return a DataFrame.

    Parameters:
        file_path (Path): The path to the input file.
        use_columns (Optional[List[str]]): A list of column names to include in the DataFrame.
                                           If None, all columns will be included.
                                           Default is None.
        reset_index (bool): Flag if want to reset index from original file.
        *kwargs (Optional[List]): Any keyword arguments to be passed to pandas reader function

    Returns:
        pd.DataFrame: A DataFrame containing the data from the input file.

    Raises:
        ValueError: If the file type is not supported.

    Note:
        Supported file formats: '.csv', '.sav', '.dta', '.pickle'.
    """
    if isinstance(file_path, str):
        file_path = Path(file_path)

    if file_path.suffix == ".csv":
        data = pd.read_csv(file_path, usecols=use_columns, *kwargs)
    elif file_path.suffix == ".sav":
        data = pd.read_spss(file_path, usecols=use_columns, *kwargs)
    elif file_path.suffix == ".dta":
        data = pd.read_stata(file_path, columns=use_columns, *kwargs)
    elif file_path.suffix == ".parquet":
        data = pd.read_parquet(file_path, columns=use_columns, *kwargs)
    elif (file_path.suffix == ".pickle") or (file_path.suffix == ".pkl"):
        data = pd.read_pickle(file_path, *kwargs)
        if use_columns is not None:
            data = data[use_columns]
    else:
        raise ValueError("File type not supported.")

    if reset_index:
        data = data.reset_index()
    return data


def sortable_key_value_dictionary(
    dictionary: dict, by_keys: bool = True, reverse: bool = False
) -> dict:
    """
    Sorts a dictionary by either keys or values in ascending or descending order.

    Args:
        dictionary (dict): The input dictionary to be sorted.
        by_keys (bool, optional): Indicates whether to sort by keys (True) or values (False). Defaults to True.
        reverse (bool, optional): Indicates whether to sort in reverse order (descending). Defaults to False.

    Returns:
        dict: The sorted dictionary.
    """
    if by_keys:
        return dict(sorted(dictionary.items(), key=lambda x: x[0], reverse=reverse))
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=reverse))


def filter_dicts_by_keys(
    dicts: List[Dict[str, any]], keys_of_interest: List[str]
) -> List[Dict[str, any]]:
    """
    Filters a list of dictionaries by keeping only the specified keys of interest.

    Args:
        dicts (List[Dict[str, any]]): The list of dictionaries to filter.
        keys_of_interest (List[str]): The list of keys to keep in each dictionary.

    Returns:
        List[Dict[str, any]]: The list of dictionaries with only the specified keys.
    """
    return [{key: d[key] for key in keys_of_interest if key in d} for d in dicts]


def xml_to_json_converter(xml_file_path: str, json_file_path: str) -> None:
    """
    Converts an XML file to JSON format and saves it to a file.

    Args:
        xml_file_path (str): The path of the XML file to convert.
        json_file_path (str): The path of the JSON file to save.

    Returns:
        None
    """
    path = Path(json_file_path)

    if not path.exists():
        # Open the XML file and read its content
        with open(xml_file_path, "r") as xml_file:
            xml_data = xml_file.read()

        # Convert XML to JSON
        json_data = json.dumps(xmltodict.parse(xml_data), indent=4)

        # Save the JSON data to a file
        with open(json_file_path, "w") as json_file:
            json_file.write(json_data)

        print("DONE! Conversion of XML to JSON...")
    else:
        print("JSON file already exits.")


def json_reader(path: str) -> dict:
    """
    Reads a JSON file and returns its content as a dictionary.

    Args:
        path (str): The path of the JSON file to read.

    Returns:
        dict: The content of the JSON file as a dictionary.
    """
    with open(path, "r") as json_file:
        data = json.load(json_file)
    return data


def reorder_columns(dataframe):
    """
    Reorders the columns of a DataFrame based on the specified list of columns to appear first.

    Parameters:
        dataframe (pd.DataFrame): The DataFrame whose columns need to be reordered.

    Returns:
        pd.DataFrame: The DataFrame with columns reordered.
    """
    columns = list(dataframe.columns)
    column_orderings = columns[:10] + ["lat_dd_mod", "lon_dd_mod"]
    for col in column_orderings:
        columns.remove(col)
    new_ordered_columns = column_orderings + columns
    return dataframe.reindex(columns=new_ordered_columns)


def saving_data_formatter(
    data: pd.DataFrame, name: str, extension: str = "csv", index: bool = False
) -> None:
    """
    Save the given DataFrame to a file in different formats based on the extension.

    Args:
        data (pd.DataFrame): The DataFrame to be saved.
        name (str): The name of the file without extension.
        extension (str, optional): The file format to save the DataFrame. Default is 'csv'.
        index (bool, optional): Whether to include the index in the saved file. Default is False.

    Returns:
        None
    """
    counter = 1

    # versioning save filename
    while True:
        saving_data_path = f"{PROCESSED_DATA_FOLDER_PATH}/{name}v{counter}.{extension}"
        if Path(saving_data_path).exists():
            counter += 1
        else:
            break

    if extension == "csv":
        data.to_csv(saving_data_path, index=index)
    elif extension == "pickle":
        data.to_pickle(saving_data_path)
    elif extension == "xlsx" or extension == "xlx":
        data.to_excel(saving_data_path, index=index)
    elif extension == "json":
        data.to_json(saving_data_path, index=index)
    else:
        print(
            "Invalid file extension. Supported extensions are 'csv', 'pickle', 'xlsx', and 'json'."
        )

    print("DONE! File has been saved successfully.")
