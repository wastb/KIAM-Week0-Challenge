# Week 0 Challenge: Solar Data Analysis

This repository contains the analysis, insights, and tools developed during the Week 0 Challenge of the 10 Academy Artificial Intelligence Mastery Program. The challenge focuses on analyzing solar radiation measurement data to derive actionable insights for optimizing solar installations.

## Project Overview

### Objective
MoonLight Energy Solutions aims to enhance operational efficiency and sustainability through data-driven solar investments. The analysis explores solar radiation, environmental conditions, and their impact on solar panel efficiency to identify high-potential regions for solar installations.

### Dataset Overview
The dataset includes environmental measurements such as solar irradiance, temperature, humidity, wind speed, and cleaning events. It covers:
- **Timestamp**: Date and time of observation.
- **GHI (Global Horizontal Irradiance)**: Total solar radiation on a horizontal surface.
- **DNI (Direct Normal Irradiance)**: Solar radiation perpendicular to the sun's rays.
- **DHI (Diffuse Horizontal Irradiance)**: Solar radiation diffused from the atmosphere.
- **Tamb**: Ambient temperature.
- **RH**: Relative humidity.
- **WS**: Wind speed and direction.
- **ModA/ModB**: Sensor readings for irradiance.
- **Cleaning**: Indicates whether a cleaning event occurred.


---

## Key Tasks and Deliverables

### 1. Exploratory Data Analysis (EDA)
- Summary statistics and data quality checks.
- Time series analysis of solar radiation and temperature.
- Impact of cleaning on sensor readings.
- Correlation analysis between solar radiation, temperature, and wind conditions.

### 2. Outlier Detection and Replacement
- Use Z-scores to identify and replace outliers with column means.

### 3. Visualizations
- **Correlation Heatmaps**: Solar radiation and temperature.
- **Pair Plots**: Wind conditions and solar irradiance.
- **Diurnal Patterns**: Hourly trends of solar radiation and temperature.
- **Wind Rose**: Wind speed and direction distribution.
- **Bubble Charts**: Multi-variable relationships between solar radiation, temperature, and humidity.

### 4. Streamlit Dashboard
Develop an interactive dashboard to visualize the data insights:
- Dynamic filtering by time and conditions.
- Interactive plots for solar trends and wind conditions.

---

## Setup and Installation

### Prerequisites
- Python 3.8 or later
- Required Python libraries (install via `requirements.txt`):
  ```bash
  pip install -r requirements.txt


