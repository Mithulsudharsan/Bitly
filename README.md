## Bitly sample Project

## Description

This project processes and analyzes URL click data from CSV and JSON files. It specifically extracts data from the year 2021, counts clicks per URL, and outputs the results in a structured format. The main functionalities include data loading, hash extraction from URLs, data filtering by date, and aggregation of click counts.

## Features

Load data from CSV and JSON.
Extract specific parts from URLs.
Filter data based on year.
Aggregate and count occurrences.

## Installation
## Prerequisites

Python 3.6 or higher
pip (Python package installer)

## Setup Environment
It is recommended to use a virtual environment to avoid conflicts with other packages and Python versions:

## Install Dependencies
pip install -r requirements.txt

## Running the Application

python src/main.py

## Data Files

Ensure that the data files encodes.csv and decodes.json are placed in the correct location

## Testing

Execute the unit tests to ensure the application functions correctly:

python -m unittest tests/test_main.py

This command runs all tests defined in test_main.py and outputs the test results.

## Authors

Mithul Sudharsan Ravikumar
