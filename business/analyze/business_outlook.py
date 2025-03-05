import pandas as pd
import numpy as np
from pathlib import Path
from .aggregate_lat_long import load_zipcodes

# define data path
data_path = Path(__file__).parent.parent / "data"

def get_macro_table():

    # Load polygons
    data_polygon = pd.DataFrame(load_zipcodes(), columns = ['zip_code','polygon'])
    data_polygon['zip_code'] = data_polygon['zip_code'].astype(int)

    # Load Macro variables:
    data_crime = pd.read_csv(data_path / "crime.csv")
    data_income = pd.read_csv(data_path / "median_income.csv")
    macro_table = data_income.merge(data_crime, how='left', on='zip_code')
    macro_table['crime_rate'] = macro_table['total_crime']*1000/macro_table['population_size']
    macro_table['theft_rate'] = macro_table['total_theft']*1000/macro_table['population_size']

    # Load data business
    data_business = calculate_changes_business()

    # Merge!    
    macro_table = macro_table.merge(data_business, how='left', on='zip_code')
    final_table = data_polygon.merge(macro_table, how='left', on='zip_code').reset_index()

    return final_table


def calculate_changes_business(year=2024):
    """
    Calculate new and closed business licenses for a given year
    """
    # load dataframes from CSV
    licenses = pd.read_csv(data_path/"licenses_duration.csv")
    licenses["initial_date"] = pd.to_datetime(licenses.initial_date)
    licenses["final_date"] = pd.to_datetime(licenses.final_date)
    
    # establish dates to compare (the first and last day)
    lower_bound = pd.Timestamp(str(year) + "-01-01")
    upper_bound = pd.Timestamp(str(year) + "-12-31")

    # filter and categorize each licenses as new, closed or existing
    licenses = licenses[(licenses.initial_date <= upper_bound) & 
                               (licenses.final_date >= lower_bound)]
    
    licenses["status"] = np.select([(licenses.initial_date >= lower_bound),
                                    (licenses.final_date <= upper_bound)],
                                   ["new", "closed"], default = "standing")
 

    # group by zipcode to calculate new and colsed by zipcode
    licenses_zip = licenses.groupby("zip_code").status.value_counts().unstack(fill_value=0)

    # Calculate rates
    licenses_zip["total"] = licenses_zip.sum(axis=1)
    licenses_zip["new_rate"] = licenses_zip.new * 100/ licenses_zip.total
    licenses_zip["closed_rate"] = licenses_zip.closed * 100/ licenses_zip.total

    return licenses_zip.reset_index()
    
    

    

    