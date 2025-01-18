# Retail Space for Lease and Mobility Trends by Codeconomics

## Members

- Hilman Hanivan <hanivan@uchicago.edu>
- Jorge Guerrero <jguerrero95@uchicago.edu>

## Title : Retail space for lease and mobility trends

## Abstract

This project aims to analyze the relationship between mobility patterns and retail space rental trends using data from the Google Mobility API and web-scraped commercial lease websites. Our goal is to provide actionable insights for business owners on optimal locations to lease retail spaces and for policymakers on underdeveloped areas requiring investment. By examining how mobility trends correlate with rent prices across different regions, we seek to highlight zones of high potential for businesses and areas that could benefit from urban development initiatives. The analysis will culminate in an interactive visualization that allows users to explore trends and make data-driven decisions. 


## Preliminary Data Sources

### Data Source #1: Google Mobility Data  
- **URL**: [Google Mobility Data](https://www.google.com/covid19/mobility/)  
- **Type**: API  
- **Challenges**:  
  - Identifying granular data for specific retail-related categories.  
  - Aligning mobility data to precise geographic boundaries (e.g., zip codes).  
  - Handling potential inconsistencies in data frequency and coverage.

### Data Source #2: Commercial Lease Data  
- **URL**: Various retail leasing websites (e.g., LoopNet, CoStar).  
- **Type**: Web scraping.  
- **Challenges**:  
  - Ensuring legality and compliance with terms of service for web scraping.  
  - Dealing with inconsistent formats and incomplete data across platforms.  
  - Cleaning and standardizing rental price data to align with mobility trends.

## Preliminary Project Plan
1. **Data Ingestion**:  
   - Integrate mobility data through the Google API.  
   - Develop a web scraping pipeline for collecting commercial lease data.  

2. **Data Cleaning and Preparation**:  
   - Standardize geographic identifiers (e.g., zip codes, coordinates) across datasets.  
   - Handle missing or inconsistent data entries.  

3. **Analysis**:  
   - Correlate mobility trends with rental prices using statistical and machine learning models.  
   - Identify high-opportunity and underdeveloped areas based on combined data.  

4. **Visualization**:  
   - Build an interactive dashboard that allows users to explore trends and findings.  
   - Include filters for geographic regions, mobility categories, and price ranges.  


## Questions  

1. What level of geographic granularity should we aim for (e.g., zip codes, neighborhoods)?  
2. Are there specific legal or ethical concerns we should address regarding web scraping?  
3. What techniques or tools do you recommend for correlating geographic data from two distinct datasets?  
4. Should we include additional data sources (e.g., census demographics, transit data) to enhance our analysis?  
5. How can we validate the accuracy of our mobility and rent correlation findings?  


