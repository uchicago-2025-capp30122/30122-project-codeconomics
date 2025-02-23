# Businesses Outlook and Economic Trends in Windy City by Codeconomics

## Members

- Hilman Hanivan <hanivan@uchicago.edu>
- Jorge Guerrero <jguerrero95@uchicago.edu>

## Abstract

This project aims to analyze businesses outlook trends in Chicago using data from businesses licenses data and crime events from the Chicago Data Portal (https://data.cityofchicago.org) and median income data from the US Census Bureau (https://www.census.gov).
Our goal is to provide insights for policymakers on understanding businesses trends in the city of Chicago, by analizing different zipcodes and industries. 


## Data Sources

### Data Reconciliation Plan

### Data Source #1: Business Licenses
Business licenses issued by the Department of Business Affairs and Consumer Protection in the City of Chicago from 2002 to the present.

- **URL**: https://data.cityofchicago.org/Community-Economic-Development/Business-Licenses/r5kz-chrr/about_data
- **Type**: API
            This is a public database taht can be requested via API without a APP_KEY
- **Unique key**: Zip Code


### Data Source #2: American Community Survey (ACS)   
The American Community Survey (ACS) is an ongoing survey that provides vital information on a yearly basis about USA population. Information from the survey generates data that help inform how trillions of dollars in federal funds are distributed each year. The ACS provies information on jobs and occupations, educational attainment, veterans, whether people own or rent their homes, and other topics. We retrieve median income data by zip code from this source. After closer examination, there exists one zipcode (60666) missing from this dataset. That being said, we have median income estimates for 58 zipcodes in Chicago!

- **URL**: https://www.census.gov/programs-surveys/acs
- **Type**: API 
    The user must get an API Key from the US Census Bureau in:  https://api.census.gov/data/key_signup.html
- **Unique key**: Zip Code

### Data Source #3: Crimes - 2001 to Present
This dataset reflects reported incidents of crime (with the exception of murders where data exists for each victim) that occurred in the City of Chicago from 2001 to present, minus the most recent seven days. From this source we will aggregate number of events by zip code.

- **URL**: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data
- **Type**: API
            This is a public database that can be requested via API without a APP_KEY
- **Unique key**: Zip Code (after cleaning)

### Data Source #4: Zipcode Boundaries 
This dataset contains 62 rows of polygons of zipcodes in Chicago. However, after close examination, there two zipcodes appear twice from the original source (60643 and 60707). That being said, we only have 59 zipcodes in Chicago! 

- **URL**: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes-Map/gdcf-axmw


## How to Run

At this step, we would just demonstrate to visualize the data of median income estimate by zipcodes from Census Bureau. The main reason why we could not demonstrate the process of getting the data is because it requires API key. Hence, let's just assume that we already have the data from pulling the repo in business/data directory!

Step 1) Run `uv sync` to sincronize the libraries.

Step 2) Run 'uv run python -m business.viz.histogram'
This will open up a browser with localhost address and the histogram of median income by zipcodes in Chicago using plotly package!

