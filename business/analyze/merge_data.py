from pathlib import Path
import pandas as pd

from .business_outlook import calculate_changes_business

def merge_data_survival():
    """
    Merge data of licenses, income and crime by zip code 
    for the survival analysis, needs duration time and event status

    Input: 
        -None but it should be runned after runningt he functions to run and 
        clean data

    Returns: 
        -licenses_merged pandas DataFrame with columns from licenses, crime and 
        income
    """
    # define data path
    data_path = Path(__file__).parent.parent / "data"

    # load dataframes from CSV
    licenses_dur = pd.read_csv(data_path/"licenses_duration.csv")
    median_income = pd.read_csv(data_path/"median_income.csv")
    crime_data = pd.read_csv(data_path/"crime.csv")

    # make the zip_code a str across the 3 dataframe
    licenses_dur["zip_code"] = licenses_dur["zip_code"].astype(str)
    median_income["zip_code"] = median_income["zip_code"].astype(str)
    crime_data["zip_code"] = crime_data["zip_code"].astype(str)

    # merge data by zipcode
    licenses_merged = (licenses_dur
                       .merge(median_income, on="zip_code", how="left")
                       .merge(crime_data, on = "zip_code", how = "left"))
    
    return licenses_merged


def merge_data_graphs():
    """
    Merge data of new and closed licenses, income and crime by zip code
    
    Input: 
        -None but it should be runned after runningt he functions to run and 
        clean data

    Returns: 
        -licenses_merged_by_zip pandas DataFrame with columns from licenses, crime and 
        income
    """
    
    # calculate data of licenses for a given year
    licenses_zip = calculate_changes_business(2024)
    
    # load dataframes from CSV
    data_path = Path(__file__).parent.parent / "data"
    median_income = pd.read_csv(data_path/"median_income.csv")
    crime_data = pd.read_csv(data_path/"crime.csv")

    # make the zip_code a str across the 3 dataframe
    licenses_zip["zip_code"] = licenses_zip["zip_code"].astype(str)
    median_income["zip_code"] = median_income["zip_code"].astype(str)
    crime_data["zip_code"] = crime_data["zip_code"].astype(str)

    # merge data by zipcode
    licenses_merged_by_zip = (licenses_zip
                       .merge(median_income, on="zip_code", how="left")
                       .merge(crime_data, on = "zip_code", how = "left"))
    
    return licenses_merged_by_zip

