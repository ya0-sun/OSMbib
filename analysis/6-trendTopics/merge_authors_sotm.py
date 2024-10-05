# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:40:04 2024

"""

import pandas as pd

# Read the Excel file
file_path = 'authors_to_merge_sotm.xlsx'  # Replace with the actual file path
df = pd.read_excel(file_path)

# Group by the 'authors' column and sum the 'articles' column
merged_df = df.groupby('Authors', as_index=False)['Articles'].sum()

# Save the merged result to a new Excel file (optional)
merged_df.to_excel('merged_authors_articles.xlsx', index=False)

# Display the merged dataframe
print(merged_df)
