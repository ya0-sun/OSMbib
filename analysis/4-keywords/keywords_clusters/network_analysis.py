# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:06:26 2024

@author: YS
"""

import pandas as pd
import re

# File paths
txt_file_path = 'network.txt'  # Replace with your txt file path
excel_file_path = 'network.xlsx'  # Replace with your desired Excel file path

def parse_columns(row):
    # Convert the last four columns from right to left
    try:
        score_avg_norm_citations = float(row[-1])
        score_avg_citations = float(row[-2])
        score_avg_pub_year = float(row[-3])
        weight_occurrences = float(row[-5])
        cluster = row[-7]  # 7th from the end
        return pd.Series([row[0], cluster, weight_occurrences, score_avg_pub_year, score_avg_citations, score_avg_norm_citations], 
                         index=['id', 'cluster', 'weight<Occurrences>', 'score<Avg. pub. year>', 'score<Avg. citations>', 'score<Avg. norm. citations>'])
    except ValueError:
        # Handle conversion errors, return None or default values
        return pd.Series([row[0], None, None, None, None, None], 
                         index=['id', 'cluster', 'weight<Occurrences>', 'score<Avg. pub. year>', 'score<Avg. citations>', 'score<Avg. norm. citations>'])

# Read the txt file into a DataFrame
try:
    # Load the data into a DataFrame
    # Assume columns are tab-separated or space-separated, adjust sep as necessary
    df = pd.read_csv(txt_file_path, sep='\t', header=None, 
                     names=['id', 'label', 'x', 'y', 'cluster', 
                            'weight<Links>', 'weight<Total link strength>', 
                            'weight<Occurrences>', 'score<Avg. pub. year>', 
                            'score<Avg. citations>', 'score<Avg. norm. citations>'])

    # Apply the parse_columns function to each row
    df_filtered = df.apply(lambda row: parse_columns(row), axis=1)

    # Write to Excel
    df_filtered.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f'The filtered data has been successfully written to {excel_file_path}')

except Exception as e:
    print(f'An error occurred: {e}')