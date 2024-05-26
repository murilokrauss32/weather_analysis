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

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

4. Install the package:
   ```bash
   pip install .

## Usage
1. Run the main script to fetch data, perform analyses, and generate visualizations:
   ```bash
   python main.py

## Analyses Performed
- Average Atmospheric Pressure:
Calculates the average pressure for the last 15 days for each specified location.

- Relationship Analysis:
Analyzes the correlation between humidity, temperature, and pressure for each location.

- Maximum Pressure Ranking:
Ranks the maximum atmospheric pressures over the last 5, 10, and 15 days across all locations.

## Visualization
- Average Pressure: Bar charts showing the average atmospheric pressure over the last 15 days for each location.
- Correlation Matrix: Heatmaps showing the correlation between humidity, temperature, and pressure for each location.
- Pressure Rankings: Bar charts showing the maximum pressures for the last 5, 10, and 15 days for each location.

## Testing
To run the tests, use the following command:
   pytest

## Results

The results of the analyses and visualizations can be found in the generated plots after running the main.py script. These include average pressure bar charts, correlation matrices, and pressure ranking bar charts.

## Dependencies
- pandas==2.0.2
- dask[dataframe]==2024.5.1
- pyarrow>=16.1.0
- matplotlib==3.9.0
- requests==2.32.2
- pytest==8.2.1
- distributed==2024.5.1
- bokeh==3.4.1

## Author
Murilo Krauss - [Your GitHub Profile](https://github.com/murilokrauss32)
