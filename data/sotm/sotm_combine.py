# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:38:54 2024

"""

import os
import csv


def format_author_name(author_name):
    # Split full name into parts (first name and last name)
    parts = author_name.strip().split()
    if len(parts) >= 2:
        # Reformat as LastName, FirstName
        last_name = parts[-1].upper()
        first_name = ' '.join(parts[:-1]).upper()
        return f"{last_name}, {first_name}"
    else:
        # In case the name format is unexpected, return it as is
        return author_name.upper()

def process_file(filename):
    # Extract the year from the filename (assuming the year is the name of the file)
    # year = os.path.splitext(os.path.basename(filename))[0]

    # List to hold the processed data
    processed_data = []

    # Read the input file
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        # Skip the first line (header) and process the rest
        for line in lines[1:]:
            line = line.strip()
            if line:
                # Split the line by commas and ignore the first part (time)
                parts = line.split(',', 2)
                if len(parts) == 3:  # Ensure we have exactly 3 parts: time, title, and author
                    title = parts[1].strip().upper()  # Second part is the title
                    authors_year = parts[2].strip()
                    
                    authors_year_parts = authors_year.split('\t') 
                    
                    authors = authors_year_parts[0].strip()
                    year = authors_year_parts[1].strip()

                    # Process each author, reformatting their name
                    formatted_authors = '; '.join(
                        format_author_name(author) for author in authors.split(';')
                    )

                    processed_data.append({
                        'TI': title,
                        'AU': formatted_authors,
                        'PY': year
                    })
                else:
                    print(f"Skipping line due to unexpected format: {line}")

    # Output CSV file name
    output_csv = "combined_data_year.csv"

    # Write the processed data to a CSV file
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['TI', 'AU', 'PY']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in processed_data:
            writer.writerow(row)

    print(f"Data successfully saved to {output_csv}")


filename = r".\sotm\combined_data_year.txt"  
process_file(filename)
