# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:50:18 2024

"""

import pandas as pd

# Read the first and second Excel files
file_path1 = 'authors_research.xlsx'  # Replace with the actual path to the first Excel file
file_path2 = 'authors_sotm.xlsx'  # Replace with the actual path to the second Excel file

df1 = pd.read_excel(file_path1)
df2 = pd.read_excel(file_path2)

# # Assuming the column with names is called 'Names' in both files
# # Check if names in the first list are in the second list
# matching_names = df1[df1['Authors'].isin(df2['Authors'])]

# # Print the matching names
# print(matching_names['Authors'].tolist())

# Assuming the column with names is called 'Names' and the column with articles is called 'Articles' in both files
# Merge the two DataFrames on the 'Names' column to find matches and get articles from both lists
merged_df = pd.merge(df1, df2, on='Authors', how='inner', suffixes=('_List1', '_List2'))

# Save the matching names and their articles to a CSV file
output_csv_path = 'matching_names_articles.csv'  # Replace with your desired output CSV file path
merged_df[['Authors', 'Articles_List1', 'Articles_List2']].to_csv(output_csv_path, index=False)


# Print the matching names and their articles from both lists
print(merged_df[['Authors', 'Articles_List1', 'Articles_List2']])
