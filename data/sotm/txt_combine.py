# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 16:22:53 2024

"""

import os

# Directory containing the text files
directory = r'.\sotm\data'
# Output file
output_file = r'.\sotm\combined_data_year.txt'

# List to hold combined lines
combined_lines = []

# Iterate over each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        year = filename.split('.')[0]  # Assuming filename is the year or contains the year
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Skip the header if present
            if combined_lines:
                lines = lines[1:]
            # Add the year to each line and append to combined_lines
            for line in lines:
                # Strip newline characters and add year at the end
                line = line.strip() + '\t' + year + '\n'
                combined_lines.append(line)

# Write the combined lines to the output file
with open(output_file, 'w') as file:
    file.writelines(combined_lines)

print(f"Combined data with year has been saved to {output_file}")
