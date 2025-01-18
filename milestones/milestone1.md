# Retail Space for Lease and Traffic Trends in Chicago by Codeconomics

## Members

- Hilman Hanivan <hanivan@uchicago.edu>
- Jorge Guerrero <jguerrero95@uchicago.edu>

## Title : Retail space for lease and mobility trends

## Abstract

This project aims to analyze the relationship between mobility patterns and retail space rental trends in Chicago using data from the Google Mobility API and web-scraped commercial lease websites (i.e. LoopNet, Regus and the Storefront). Our goal is to provide insights for business owners on optimal locations to lease retail spaces and for policymakers on underdeveloped areas requiring investment. By examining how mobility trends correlate with rent prices across different neighborhoods, we seek to highlight zones of high potential for businesses and areas that could benefit from urban development initiatives. The analysis will include in an interactive visualization that allows users to explore trends and make data-driven decisions. 


## Preliminary Data Sources

### Data Source #1: Mobility / Traffic Data  
- **URL**: Placer ai(https://www.placer.ai/foot-traffic-analytics)  - foot traffic data priced
            Chicago Traffic Tracker (https://data.cityofchicago.org/Transportation/Chicago-Traffic-Tracker-Historical-Congestion-Esti/sxs8-h27x/about_data) - car traffic free
            Open street map (https://www.openstreetmap.org/#map=19/45.468440/-122.653214) - open source
            Best time app (https://besttime.app/subscription/pricing#pricing) - foot traffic freemium
- **Type**: API
- **Challenges**:  
  - Identifying granular data for specific retail-related categories, getting mobility data for free/affordable.  
  - Aligning mobility data to precise geographic boundaries (e.g., zip codes).  
  - Handling potential inconsistencies in data frequency and coverage.

### Data Source #2: Commercial Lease Data  
- **URL**: Various retail leasing websites (e.g., i.e. LoopNet, Regus and the Storefront).
            (https://www.loopnet.com/search/retail-space/chicago-il/for-lease/?sk=0c6e47de415ea6518eda879a142f51f2)
            (https://www.thestorefront.com/search?address=Chicago,%20IL,%20USA&zoom=10.708618128466517&latitude=41.8781136&longitude=-87.6297981999999&lat_g=41.66474041679231&lat_l=42.04965634866119&lng_g=-87.76893824851147&lng_l=-87.28491106800573&s=score%20DESC&country=United%20States&city=Chicago&page=1)
            (https://www.propertyshark.com/cre/retail/us/il/chicago/)

- **Type**: Web scraping.  
- **Challenges**:   
  - Dealing with inconsistent formats and incomplete data across platforms, specially for geolocalization (coordinates, zipcodes).  
  - Cleaning and standardizing rental price data to align with mobility/traffic trends.

## Preliminary Project Plan
1. **Data Ingestion**:  
   - Integrate mobility data from the chosen source (pedestrian/foot traffic data).
   - Develop a web scraping pipeline for collecting commercial lease data.  

2. **Data Cleaning and Preparation**:
   - Standardize geographic identifiers (e.g., zip codes, coordinates) across datasets.  
   - Handle missing or inconsistent data entries.  

3. **Analysis**:  
   - Correlate mobility trends with rental prices using statistical and/or other models.  
   - Identify high-opportunity and underdeveloped areas based on combined data.  

4. **Visualization**:  
   - Build an interactive dashboard that allows users to explore trends and findings.  
   - Include filters for neighborhoods, mobility categories, and price ranges.  


## Questions  

1. Do you know of a data source with pedestrian/foot traffic that we can use? Perhaps a U Chicago partnership?
2. What level of geographic granularity should we aim for (e.g., zip codes, neighborhoods)?  
3. Are there specific legal or ethical concerns we should address regarding web scraping?  
4. What techniques or tools do you recommend for correlating geographic data from two distinct datasets?  
5. Should we include additional data sources (e.g., census demographics, transit data) to enhance our analysis?  

