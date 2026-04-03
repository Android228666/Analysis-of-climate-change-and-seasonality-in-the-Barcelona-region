# Climate Change and Seasonality Analysis in the Barcelona Region

## Project Overview
This project focuses on the descriptive and diagnostic analysis of climate changes in the Barcelona region using **ERA5 reanalysis data** (1994–2024). The study investigates temperature trends, changing seasonality (specifically the lengthening of summer), and the frequency of extreme weather events. Additionally, it evaluates the effectiveness of machine learning methods in interpreting these climatic shifts.

**Author:** Andrii Khomenko  
**Field of Study:** Data Science (IAD), 3rd Year  
**Context:** Machine Learning Course Project

## Key Research Hypotheses
1. **Warming Trends:** Systematic warming of the region, particularly during the summer season.
2. **Seasonality Shifts:** Significant lengthening of the summer season and an increase in extremely warm days.
3. **Precipitation Dynamics:** While total annual rainfall remains stable, there is a shift toward short-term, high-intensity precipitation episodes (especially in autumn).
4. **Machine Learning Utility:** ML models can identify seasonal dependencies, though their predictive power is limited by the natural variability of the climate system.

## Data Source
The analysis utilizes the **ERA5 reanalysis** dataset provided by the **Copernicus Climate Data Store (CDS)**. 
- **Timeframe:** 1994 – 2024 (30 years of daily data).
- **Location:** Barcelona coastal region (Bounding Box: `[41.6, 2.0, 41.1, 2.4]`).
- **Variables:** - 2m Temperature & Dewpoint Temperature
  - Total Precipitation
  - Surface Solar & Thermal Radiation
  - Wind Components (10m u/v)
  - Surface Pressure

## Project Structure
- `Kod_pobrania_danych.py`: Python script utilizing the `cdsapi` to automate the retrieval of NetCDF files from the Copernicus CDS.
- `Notebook_roboczy.html`: The core analytical workspace containing data cleaning, exploratory data analysis (EDA), visualization, and machine learning model implementation.
- `Finalne_sprawozdanie.pdf`: The comprehensive final report documenting methodology, results, and conclusions.

## Methodology
The project follows a standard data science pipeline:
1. **Data Acquisition:** Automated retrieval of atmospheric data via API.
2. **Preprocessing:** Handling NetCDF formats, aggregating hourly data to daily/monthly averages, and feature engineering for seasonality.
3. **Analysis:** Trend estimation using statistical methods and visualization of temperature anomalies.
4. **Modeling:** Applying Machine Learning techniques to identify patterns in seasonal transitions and extreme event occurrences.

## Main Findings
- [cite_start]**Temperature:** A clear upward trend in temperatures was confirmed, with summer becoming increasingly intense[cite: 1].
- [cite_start]**Summer Duration:** Observations indicate a measurable extension of the summer period[cite: 1].
- [cite_start]**Extreme Events:** Increased frequency of extremely hot days and heavy rainfall bursts[cite: 1].
- [cite_start]**Limitations:** ERA5 data provides a smoothed spatial average, which may slightly underestimate local urban heat island effects or hyper-local extremes[cite: 1].

## Requirements
To run the data collection script, you will need:
- Python 3.x
- `cdsapi` library
- A valid CDS API Key (configured in `.cdsapirc` or within the script)

```bash
pip install cdsapi
