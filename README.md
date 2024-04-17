## Bitly sample Project

## Description

This project processes and analyzes URL click data from CSV and JSON files. It specifically extracts data from the year 2021, counts clicks per URL, and outputs the results in a structured format. The main functionalities include data loading, hash extraction from URLs, data filtering by date, and aggregation of click counts.

## Features

Load data from CSV and JSON.
Extract specific parts from URLs.
Filter data based on year.
Aggregate and count occurrences.

## Prerequisites

Python 3.6 or higher
pip (Python package installer)
Virtualenv (recommended)
Docker (optional for containerization)

## Installation
Clone the Repository

git clone https://github.com/yourusername/bitly_project.git
cd bitly_project

## Setup Environment
It is recommended to use a virtual environment to avoid conflicts with other packages and Python versions:

## Creating a Virtual Environment
Open your command line or terminal and Navigate to your project directory where you want the virtual environment to be created.
Run the virtual environment creation command

python -m venv .venv
source .venv/bin/activate (mac os and linux)
.venv\Scripts\activate.bat (Windows)

## Install Dependencies
pip install -r requirements.txt

## Data Folder

Decode.json and encodes.csv are the 2 data files we are using for opperations

## Log_Files

All the Logs related to the application as well as testing status is been generated to the respective files 


## THE PROJECT FILE HAS 2 MAIN.PY THAT IS (MAIN CODE.PY) IS RETURN THE OUTPUT TO THE TERMINAL IN JSON FORMAT  (MAIN.PY) IS BUILD USING SIMPLE FLASK FRAMEWORK TO VISUALIZE SAME JSON OUTPUT IN SIMPLE WEB PAGE TO HAVE A GUI VIEW



## Running the MAIN CODE.PY To see answer in Terminal
python3 src/main.py

## To Run MAIN.PY Application
## Set the FLASK_APP Environment Variable
export FLASK_APP=path_to_your_app.py (Mac or Linux)
set FLASK_APP=path_to_your_app.py (windows)

## Update the file Path
It is important to update the your path to the JSON,CSV location

## To Run MAIN.PY Application 
flask run 
## Access the Application
http://localhost:5001


## Testing

Execute the unit tests to ensure the application functions correctly:

python -m unittest tests/test_main.py

This command runs all tests defined in test_main.py and outputs the test results.


## Docker Repo

https://hub.docker.com/r/mithulsudharsan/bitly/tags

##  Run The application As Docker Image (Optional)

Install Docker Desktop for Convenient Access

Pull the Docker Image

•	docker pull mithulsudharsan/bitly_project:latest

Run the Docker Image
•	docker run -p 5001:5001 --name bitly_project_instance yourusername/bitly_project:latest

Access the Application

•	http://localhost:5001

Stop and Remove the Container

•	docker stop bitly_project_instance
•	docker rm bitly_project_instance


## Authors

Mithul Sudharsan Ravikumar

## COLAB Link 

https://colab.research.google.com/drive/1J-cT4rR-FSPadrCLLAunn2Ln7dVXoksD?authuser=2#scrollTo=ZiGxLN1-XHDS
