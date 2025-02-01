# Retail Space for Lease and Economic Trends in Chicago by Codeconomics

## Members

- Hilman Hanivan <hanivan@uchicago.edu>
- Jorge Guerrero <jguerrero95@uchicago.edu>

## Title : Retail space for lease and economic trends

## Abstract

This project aims to analyze the relationship between retail space rental trends in Chicago using data from web-scraped commercial lease websites (i.e. Storefront), economic indicators from the Census Bureau. Our goal is to provide insights for business owners on optimal locations to lease retail spaces and for policymakers on underdeveloped areas requiring investment. By examining how rent prices across different neighborhoods, we seek to highlight zones of high potential for businesses and areas that could benefit from urban development initiatives. 


## Data Sources

### Data Reconciliation Plan

### Data Source #1: Commercial Lease Data  
- **URL**: Retail leasing websites (Storefront)
            (https://www.thestorefront.com/search?address=Chicago,%20IL,%20USA&zoom=10.708618128466517&latitude=41.8781136&longitude=-87.6297981999999&lat_g=41.66474041679231&lat_l=42.04965634866119&lng_g=-87.76893824851147&lng_l=-87.28491106800573&s=score%20DESC&country=United%20States&city=Chicago&page=1)
            (https://www.propertyshark.com/cre/retail/us/il/chicago/)

- **Type**: Web scraping. 
- **Unique key**: Zip Code
- **Size**: Storefront has 36 properties; LoopNet has 500+ properties; PropertyShark 1700 properties
- **Columns**: zip code, adress, squared feet, price, year build, type of property, walk score, transit score, bike score
- **Challenges**:   
- We were able to scrap webpage from storefront. However,  we found a HTTP 403 refused request from Property Shark (might have a way around), but loopnet the timeout was exceeded we could not scrap their webpage.
- We need help to find out if we can fetch data from PropertyShark or Loopnet that hold a bigger dataset. 



### Data Source #2: County Business Patterns (CBP) and ZIP Codes Business Patterns (ZBP) from US Census Bureau   
County Business Patterns (CBP) is an annual series that provides subnational economic data for establishments with paid employees by industry and employment size. This series includes the number of establishments, employment during the week of March 12, first quarter payroll, and annual payroll.
- **URL**: https://www.census.gov/data/developers/data-sets/cbp-zbp.html
- **Type**: API 
- **Unique key**: Zip Code
- **Size**: 28 variables for all zipcodes
- **Columns**: zip code, year, state, NAICS economic sector, industry, annual payroll, number of establishments, number of employees (https://api.census.gov/data/2022/cbp/variables.html)

- **Challenges**:   
- Data is from 2022 and might be outdated.


## Project Plan

1. **Data Ingestion [WEEK 5-6]**:  
   - Develop a web scraping pipeline for collecting commercial lease data 
   - Get API Key for census bureau and fetch data 

2. **Data Cleaning and Preparation [WEEK 6-7]**:
   - Standardize geographic identifiers (e.g., zip codes) to merge data.  
   - Handle missing or inconsistent data entries from webscrapping.  

3. **Analysis [WEEK 7-8]**:  
   - Correlate rental prices with statistical variables.  
   - Identify high-opportunity and underdeveloped areas based on combined data.  

4. **Visualization [WEEK 7-8]**:  
   - Build an interactive dashboard that allows users to explore trends and findings.  
   - [OPTIONAL] Include filters for neighborhoods and price ranges. 

## Questions

1. We will reach the course staff for finding a way to fetch data from PropertyShark