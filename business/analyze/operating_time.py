import pandas as pd
from pathlib import Path

def operating_time(licenses_data: Path, date_filter = "2021-01-01"):
    """
    Calculates operating time of a license (dif between initial date and 
    revoked date) 
    """
    licenses = pd.read_json(licenses_data, orient="records")

    licenses["license_start_date"] = pd.to_datetime(licenses["license_start_date"])
    licenses["license_status_change_date"] = pd.to_datetime(licenses["license_status_change_date"])

    # group by license_number: Each license has a single license number 
    # that stays consistent throughout the lifetime of the license. 
    licenses_dur = licenses.groupby("license_number").agg(
        initial_date=("license_start_date", "min"),
        final_date=("license_status_change_date", "max")
        ).reset_index()
    
    # (OPTIONAL) filter data for initial date greater than 2020
    licenses_dur = licenses_dur[licenses_dur.initial_date >= date_filter]

    # make new variables of duration and dummy if the business closed
    licenses_dur["closed"] = licenses_dur["final_date"].notna().astype(int)

    today = pd.Timestamp.today()
    licenses_dur["duration"] = licenses_dur.apply(
        lambda row: (row["final_date"] - row["initial_date"]).days 
        if row["closed"] == 1 
        else (today - row["initial_date"]).days, 
        axis=1
    )

    # make a df with unique characteristics by license_number and join it

    business_char = (licenses[["license_number",
                               "doing_business_as_name",
                               "city",
                               "state",
                               "zip_code",
                               "neighborhood",
                               "license_description",
                               "business_activity"]]
                     .drop_duplicates())
    
    
    licenses_dur = licenses_dur.merge(business_char, on="license_number", how="left")
    
    output_filename = Path(__file__).parent.parent / "data/licenses_duration.csv"
    licenses_dur.to_csv(output_filename, index=False)

