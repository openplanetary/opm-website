import csv
import json
import os

# Input and output file paths
csv_file_path = os.path.join('assets', 'basemaps.csv')
json_file_path = os.path.join('assets', 'basemaps.json')

# Read CSV file and convert to JSON
basemaps = []
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Convert TMS Option to boolean
        if row['TMS Option'].lower() == 'true':
            row['TMS Option'] = True
        elif row['TMS Option'].lower() == 'false':
            row['TMS Option'] = False
        
        # Convert Preliminary to boolean if it exists and has a value
        if 'Preliminary' in row and row['Preliminary'].lower() == 'true':
            row['Preliminary'] = True
        elif 'Preliminary' in row and row['Preliminary'].lower() == 'false':
            row['Preliminary'] = False
        
        # Convert Datasets to array if it contains values
        if 'Datasets' in row and row['Datasets']:
            row['Datasets'] = [dataset.strip() for dataset in row['Datasets'].split(';')]
        else:
            row['Datasets'] = []
        
        basemaps.append(row)

# Write to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(basemaps, json_file, indent=2)

print(f"Conversion complete. JSON file created at: {json_file_path}")