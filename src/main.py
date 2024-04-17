import pandas as pd
import json
import os
import logging
from flask import Flask

# Initialize a Flask application
app = Flask(__name__)

def load_data(encodes_path, decodes_path):
    # Load CSV data into a DataFrame
    encodes = pd.read_csv(encodes_path)
    # Load JSON data into a dictionary and convert to DataFrame
    with open(decodes_path, 'r') as file:
        decodes = json.load(file)

    logging.info("data loaded")
    return encodes, pd.DataFrame(decodes)

def extract_hash(bitlink):
    # Extract the hash part of a bitly link which is typically after the last '/'
    return bitlink.split('/')[-1]

def filter_and_map_data(encodes, decodes):
    # Convert timestamp strings in the 'decodes' DataFrame to datetime objects
    decodes['timestamp'] = pd.to_datetime(decodes['timestamp'])
    # Filter the DataFrame to include only entries from the year 2021
    filtered_decodes = decodes[decodes['timestamp'].dt.year == 2021].copy()
    # Apply the 'extract_hash' function to each bitlink to extract hashes
    filtered_decodes.loc[:, 'hash'] = filtered_decodes['bitlink'].apply(extract_hash)
    # Merge the 'encodes' DataFrame with the 'filtered_decodes' on the hash column
    return filtered_decodes.merge(encodes, how='left', on='hash')

def count_clicks(mapped_clicks):
    # Count occurrences of each URL and return a DataFrame sorted by counts
    click_counts = mapped_clicks['long_url'].value_counts().reset_index()
    click_counts.columns = ['long_url', 'count']
    return click_counts.sort_values(by='count', ascending=False)

def format_output(sorted_clicks):
    """
    Convert the sorted click data into a JSON-compatible format.
    
    Parameters:
        sorted_clicks (DataFrame): DataFrame containing sorted click counts.
    
    Returns:
        list: A list of dictionaries, each containing a URL and its click count.
    """
    # Convert DataFrame to a list of dictionaries
    result = [{row['long_url']: int(row['count'])} for _, row in sorted_clicks.iterrows()]
    return result


@app.route('/')
def index():
    # Set up basic configuration for logging
    logging.basicConfig(level=logging.INFO)
    try:
        # Load data
        encodes, decodes = load_data('/Users/mithulsudharsanravikumar/Downloads/bitly/data/encodes.csv', '/Users/mithulsudharsanravikumar/Downloads/bitly/data/decodes.json')
        # Process data
        mapped_clicks = filter_and_map_data(encodes, decodes)
        # Count clicks
        sorted_clicks = count_clicks(mapped_clicks)
        # Generate HTML table
        html_table = format_output(sorted_clicks)
        return html_table
    except Exception as e:
        # Log any errors that occur
        logging.error(f"An error occurred: {e}")
        return f"An error occurred: {e}"
import logging

def setup_logging():
    log_directory = '/Users/mithulsudharsanravikumar/Downloads/bitly/log_files'
    log_file = os.path.join(log_directory, 'app.log')

    # Check if the directory exists, if not, create it
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    logging.basicConfig(
        filename=log_file,  # Use the full path to the log file
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

setup_logging()


# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
