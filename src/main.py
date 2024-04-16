import pandas as pd
import json
import logging

def load_data(encodes_path, decodes_path):
    encodes = pd.read_csv(encodes_path)
    with open(decodes_path, 'r') as file:
        decodes = json.load(file)
    return encodes, pd.DataFrame(decodes)

def extract_hash(bitlink):
    return bitlink.split('/')[-1]

def filter_and_map_data(encodes, decodes):
    decodes['timestamp'] = pd.to_datetime(decodes['timestamp'])
    filtered_decodes = decodes[decodes['timestamp'].dt.year == 2021].copy()
    filtered_decodes.loc[:, 'hash'] = filtered_decodes['bitlink'].apply(extract_hash)
    return filtered_decodes.merge(encodes, how='left', on='hash')

def count_clicks(mapped_clicks):
    click_counts = mapped_clicks['long_url'].value_counts().reset_index()
    click_counts.columns = ['long_url', 'count']
    return click_counts.sort_values(by='count', ascending=False)

def format_output(sorted_clicks):
    return [{row['long_url']: int(row['count'])} for _, row in sorted_clicks.iterrows()]

def main():
    logging.basicConfig(level=logging.INFO)
    try:
        encodes, decodes = load_data('data/encodes.csv', 'data/decodes.json')
        mapped_clicks = filter_and_map_data(encodes, decodes)
        sorted_clicks = count_clicks(mapped_clicks)
        print(json.dumps(format_output(sorted_clicks), indent=4))
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
