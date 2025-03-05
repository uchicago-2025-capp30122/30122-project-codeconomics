import pandas as pd
from pathlib import Path


def operating_time(licenses_data: Path, date_filter=True):
    """
    Calculates operating time of a license (dif between initial date and
    expiration date)
    """
    licenses = pd.read_json(licenses_data, orient="records")

    licenses["license_start_date"] = pd.to_datetime(licenses.license_start_date)
    licenses["expiration_date"] = pd.to_datetime(
        licenses.expiration_date, errors="coerce"
    )

    # group by license_number: Each license has a single license number
    # that stays consistent throughout the lifetime of the license.
    licenses_dur = (
        licenses.groupby("license_number")
        .agg(
            initial_date=("license_start_date", "min"),
            final_date=("expiration_date", "max"),
        )
        .reset_index()
    )

    # filter data for initial date greater than 2020.
    # Used for testing the dataframe with fewer data
    if date_filter:
        licenses_dur = licenses_dur[licenses_dur.initial_date >= "2020-01-01"]

    # make new variables of duration and dummy if the business closed.
    # This date considers the final date of the analysis is feb 2025.
    licenses_dur["closed"] = (licenses_dur.final_date <= "2025-02-28").astype(int)

    today = pd.Timestamp.today()
    licenses_dur["duration"] = licenses_dur.apply(
        lambda row: (row["final_date"] - row["initial_date"]).days
        if row["closed"] == 1
        else (today - row["initial_date"]).days,
        axis=1,
    )

    # filter cases that are inconsistent from the data source
    # (earlier expiration dates than date of issue, 297 cases of 34,343)
    licenses_dur = licenses_dur[(licenses_dur.duration > 0)]

    # make a df with unique characteristics by license_number and join
    # it with the duration df.
    business_char = licenses[
        [
            "license_number",
            "doing_business_as_name",
            "city",
            "state",
            "zip_code",
            "neighborhood",
            "license_description",
            "business_activity",
            "latitude",
            "longitude",
        ]
    ].drop_duplicates()

    licenses_dur = licenses_dur.merge(business_char, on="license_number", how="left")

    # write the output CSV to be used in next steps
    output_filename = Path(__file__).parent.parent / "data/licenses_duration.csv"
    licenses_dur.to_csv(output_filename, index=False)
