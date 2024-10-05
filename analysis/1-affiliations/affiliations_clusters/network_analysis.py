# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:06:26 2024

"""

import pandas as pd
import re

# File paths
txt_file_path = 'network.txt'  
excel_file_path = 'network_aff.xlsx'  

def parse_columns(row):
    # Convert the last four columns from right to left
    try:
        score_avg_norm_citations = float(row[-1])
        score_avg_citations = float(row[-2])
        score_avg_pub_year = float(row[-3])
        weight_citation = float(row[-5])
        weight_documents = float(row[-6])
        cluster = row[-9]  # 7th from the end
        return pd.Series([row[0], cluster, weight_documents, weight_citation, score_avg_pub_year, score_avg_citations, score_avg_norm_citations], 
                         index=['id', 'cluster', 'weight<Documents>', 'weight<Citations>', 'score<Avg. pub. year>', 'score<Avg. citations>', 'score<Avg. norm. citations>'])
    except ValueError:
        # Handle conversion errors, return None or default values
        return pd.Series([row[0], None, None, None, None, None], 
                         index=['id', 'cluster', 'weight<Documents>', 'weight<Citations>', 'score<Avg. pub. year>', 'score<Avg. citations>', 'score<Avg. norm. citations>'])
        

# Read the txt file into a DataFrame
try:
    # Load the data into a DataFrame
    # Assume columns are tab-separated or space-separated, adjust sep as necessary
    df = pd.read_csv(txt_file_path, sep='\t', header=0, 
                     names=['label', 'x', 'y', 'cluster', 'weight<Links>', 'weight<Total link strength>', 'weight<Documents>',
                            'weight<Citations>', 'weight<Norm. citations>', 
                            'score<Avg. pub. year>', 
                            'score<Avg. citations>', 'score<Avg. norm. citations>'])

    # Apply the parse_columns function to each row
    df_filtered = df.apply(lambda row: parse_columns(row), axis=1)

    # Write to Excel
    df_filtered.to_excel(excel_file_path, index=False, engine='openpyxl')

    print(f'The filtered data has been successfully written to {excel_file_path}')

except Exception as e:
    print(f'An error occurred: {e}')
