from pathlib import Path
import pandas as pd

def merge_data_survival():
    """
    Merge data of licenses, income and crime by zip code 
    for the survival analysis, needs duration time and event status

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
    Merge data of licenses, income and crime by zip code
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

