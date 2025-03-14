# Daylight-Saving-Calculator

Welcome to **Daylight Saving Calculator**, a Python-based tool that helps you find the optimal fixed time offset for your location to maximize sunlight hours between your desired sunrise and sunset times—perfect for imagining a world without Daylight Saving Time (DST). This project includes a web interface hosted on GitHub Pages where users can input their preferences and see the results.

## Project Overview

The idea behind SunTime Optimizer is simple: if we abolished DST and stuck to a single time all year, what time offset (relative to UTC or standard time) would best align the sun’s rise and set with your ideal schedule? For example, if you want the sun to rise at 7:00 AM and set at 7:00 PM, this tool calculates the best fixed offset to maximize sunlight within that window throughout the year.

### Features

- Input your desired sunrise and sunset times.
- Specify your location (latitude and longitude).
- Get a recommended time offset and see how sunrise/sunset times vary across the year.
- Web interface for easy access, hosted on GitHub Pages. (TBI)

### Use Case

- Personalize your ideal "no-DST" time zone.
- Explore how sunlight patterns change with different offsets.
- Educational tool for understanding solar time and timekeeping.

## Demo

Check out the live demo on [GitHub Pages]() (link to be added once deployed).

## Installation

To run this project locally or contribute to its development, follow these steps:

### Prerequisites

- Python 3.8+
- Git
 
### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/macphersoncole/Daylight-Saving-Calculator.git
    cd Daylight-Saving-Calculator
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
  
    The `requirements.txt` file includes:
    
    ```text
    astral==2.2
    pytz==2023.3
    ```

4. Run the Python script:

    ```bash
    python Daylight_Saving_Calculator.py
    ```
    
    This will calculate the optimal offset for a hardcoded example (e.g., New York City, sunrise at 7:00 AM, sunset at 7:00 PM). Modify the script to test your own inputs.

## Usage

### Command Line

Edit `Daylight_Saving_Calculator.py` with your desired sunrise, sunset, and location:

```Python
desired_sunrise = "07:00"
desired_sunset = "19:00"
latitude = 40.7128  # e.g., New York City
longitude = -74.0060
```

Run the script to see the recommended offset and sample sunrise/sunset times.

### Web Interface (TBI)
1. Open the GitHub Pages site (once deployed).
2. Enter your desired sunrise and sunset times (e.g., "07:00" and "19:00").
3. Input your latitude and longitude (e.g., 40.7128, -74.0060 for NYC).
4. Click "Calculate" to view your optimal time offset and a summary of results.

## How It Works

1. **Solar Calculations**: Uses the `astral` library to compute sunrise and sunset times for every day of the year based on your location.
2. **Offset Testing**: Tests a range of time offsets (e.g., -12 to +12 hours in 15-minute increments).
3. **Scoring**: Measures how much sunlight falls between your desired sunrise and sunset times, selecting the offset with the highest score.
4. **Output**: Provides the best offset and examples of sunrise/sunset times throughout the year.

## Project Structure

```text
suntime-optimizer/
├── suntime_optimizer.py  # Core Python script for calculations
├── index.html            # GitHub Pages frontend
├── styles.css            # (Optional) Styling for the web interface
├── script.js             # (Optional) JavaScript for frontend logic
├── data/                 # (Optional) Precomputed results or lookup tables
├── requirements.txt      # Python dependencies
└── README.md             # This file
```
