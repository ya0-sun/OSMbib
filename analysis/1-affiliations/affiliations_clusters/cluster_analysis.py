import json
import pandas as pd

# File paths
json_file_path = 'affiliations.json'  
excel_file_path = 'items_affi.xlsx'   

# Function to extract valid JSON from a file
def extract_json_content(file_path):
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        # Read the entire file content
        file_content = file.read()
        
        # Attempt to find the start and end of the JSON object
        start = file_content.find('{')
        end = file_content.rfind('}') + 1
        
        # Extract and return the JSON string
        json_string = file_content[start:end]
        return json_string

# Read and parse the JSON content
try:
    json_string = extract_json_content(json_file_path)
    data = json.loads(json_string)
except json.JSONDecodeError as e:
    print(f'Error decoding JSON: {e}')
    exit()

# Check if 'items' field exists in the JSON data
# if 'items' in data:
items = data['network']['items']

# Extract data
item_ids = [item.get('id', '') for item in items]
labels = [item.get('label', '') for item in items]
clusters = [item.get('cluster', '') for item in items]

# Create a DataFrame
df = pd.DataFrame({
    'ID': item_ids,
    'Label': labels,
    'Cluster': clusters
})

# Write to Excel
df.to_excel(excel_file_path, index=False, engine='openpyxl')

print(f'Items have been successfully written to {excel_file_path}')
