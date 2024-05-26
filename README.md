# Weather Analysis Project

## Description
This project fetches weather data from various locations using the ThingSpeak API and performs various analyses, including calculating average atmospheric pressure, analyzing the relationship between humidity, temperature, and pressure, and ranking the maximum pressures over different periods. The results are visualized using matplotlib and Dask is used for parallel computation to handle the data efficiently.

## Project Structure
weather_analysis/
├── .gitignore
├── config.py
├── main.py
├── README.md
├── requirements.txt
├── setup.py
├── src/
│ ├── analysis.py
│ ├── data_fetcher.py
│ ├── visualization.py
│ ├── init.py
└── tests/
├── test_analysis.py
├── test_data_fetcher.py
├── test_visualization.py


### Files and Directories
- **config.py**: Contains configuration variables like the channel IDs for different locations.
- **main.py**: The main script that orchestrates data fetching, analysis, and visualization.
- **README.md**: This file, providing an overview of the project.
- **requirements.txt**: Lists the dependencies required to run the project.
- **setup.py**: Setup script for installing the package.
- **src/**: Contains the core modules for data fetching, analysis, and visualization.
  - **analysis.py**: Functions to perform various analyses on the weather data.
  - **data_fetcher.py**: Functions to fetch data from the ThingSpeak API.
  - **visualization.py**: Functions to generate visualizations of the analysis results.
  - **__init__.py**: Marks the directory as a Python package.
- **tests/**: Contains unit tests for the core modules.
  - **test_analysis.py**: Unit tests for `analysis.py`.
  - **test_data_fetcher.py**: Unit tests for `data_fetcher.py`.
  - **test_visualization.py**: Unit tests for `visualization.py`.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather_analysis.git
   cd weather_analysis
