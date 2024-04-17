import pandas as pd
import json
import logging
"""
    Load data from CSV and JSON files into pandas DataFrames.
    
    Args:
        encodes_path: A string path to the CSV file.
        decodes_path: A string path to the JSON file.
        
    Returns:
        A tuple of pandas DataFrames: (encodes, decodes)
"""
def load_data(encodes_path, decodes_path):
    try:
        # Read the CSV file 
        encodes = pd.read_csv(encodes_path)
        # Open the JSON file 
        with open(decodes_path, 'r') as file:
            decodes = json.load(file)
        # Log a message indicating the data was loaded successfully
        logging.info("Data successfully loaded from files.")
        # Return the CSV data as a DataFrame and the JSON data as a DataFrame
        return encodes, pd.DataFrame(decodes)
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logging.error(f"Failed to load data: {e}")
        raise

"""
    Extract the hash part of a bitly link.
    
    Args:
        bitlink: A string of the bitly URL.
    
    Returns:
        The extracted hash as a string.
    """
def extract_hash(bitlink):
    # Split the bitlink URL at '/' and return the last element (hash part)
    return bitlink.split('/')[-1]

"""
    Filter the decodes data to include only entries from 2021
    and map it to the encodes data on the 'hash' key.
    
    Args:
        encodes: A DataFrame containing the encodes data.
        decodes: A DataFrame containing the decodes data.
        
    Returns:
        A merged DataFrame after filtering and mapping.
    """
def filter_and_map_data(encodes, decodes):
    try:
        # Convert 'timestamp' strings in 'decodes' DataFrame to datetime objects
        decodes['timestamp'] = pd.to_datetime(decodes['timestamp'])
        # Filter out the data to include only the entries from the year 2021
        filtered_decodes = decodes[decodes['timestamp'].dt.year == 2021].copy()
        # Apply the extract_hash function to create a new column 'hash'
        filtered_decodes.loc[:, 'hash'] = filtered_decodes['bitlink'].apply(extract_hash)
        # Merge the 'encodes' DataFrame with 'filtered_decodes' on the 'hash' column
        result = filtered_decodes.merge(encodes, how='left', on='hash')
        # Log a message indicating the success of the filtering and mapping
        logging.info("Data filtered and mapped successfully.")
        return result
    except Exception as e:
        # Log any exceptions that occur and re-raise them
        logging.error(f"Error during data filtering and mapping: {e}")
        raise

# Function to count the number of clicks for each URL
def count_clicks(mapped_clicks):
    # Count occurrences of each unique 'long_url' and sort them by count in descending order
    click_counts = mapped_clicks['long_url'].value_counts().reset_index()
    # Rename the columns of the resulting DataFrame for clarity
    click_counts.columns = ['long_url', 'count']
    return click_counts.sort_values(by='count', ascending=False)

# Function to format the output into a JSON structure
def format_output(sorted_clicks):
    # Create a list of dictionaries from the DataFrame
    return [{row['long_url']: int(row['count'])} for _, row in sorted_clicks.iterrows()]

"""
    Configure logging to output to a file with a specified format and level.
"""
def setup_logging():
    # Configure the logging to file with the specified level and format
    logging.basicConfig(
        filename='/Users/mithulsudharsanravikumar/Downloads/bitly/log_files/app.log',  # Log to a file named 'app.log'
        level=logging.INFO,  # Set the log level to INFO
        format='%(asctime)s - %(levelname)s - %(message)s',  # Define the log message format
        datefmt='%Y-%m-%d %H:%M:%S'  # Define the date format for logging
    )

# Initialize logging
setup_logging()

"""
    The main function that loads data, processes it and prints the JSON output.
"""
def main():
    # Set the logging level to INFO (overriding previous configurations if any)
    logging.basicConfig(level=logging.INFO)
    try:
        # Load the data using the load_data function
        encodes, decodes = load_data('/Users/mithulsudharsanravikumar/Downloads/bitly/data/encodes.csv', '/Users/mithulsudharsanravikumar/Downloads/bitly/data/decodes.json')
        # Filter and map the data using the filter_and_map_data function
        mapped_clicks = filter_and_map_data(encodes, decodes)
        # Count the clicks using the count_clicks function
        sorted_clicks = count_clicks(mapped_clicks)
        # Print the formatted output
        print(json.dumps(format_output(sorted_clicks), indent=4))
    except Exception as e:
        # Log any exceptions that occur
        logging.error(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
