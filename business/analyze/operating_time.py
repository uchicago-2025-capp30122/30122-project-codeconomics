import json
import pandas as pd
from pathlib import Path

def operating_time(licenses_data: Path):
    """
    Calculates operating time of an account
    """
    licenses = pd.read_json(licenses_data, orient="records")

    # Filter data for year operating greater than 2020

    # license_number: The license number known to the public.
    # This is the field most users will want for most purposes. 
    # Each license has a single license number that stays consistent throughout 
    # the lifetime of the license. 

    # Group data by license_number to get min date and date end operation. if end operation does not exist, 
    # mark it as today or very early
    # Take difference of dates min and date max returning a lsit of dic (json_file)
    #
    # 
    # 