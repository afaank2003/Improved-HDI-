import pandas as pd
import numpy as np
import zipfile
import os

# Define the paths to the data files
hdi_file_path = '/mnt/data/HDR23-24_Statistical_Annex_HDI_Table.xlsx'
gdi_file_path = '/mnt/data/HDR23-24_Statistical_Annex_GDI_Table.xlsx'
gpi_zip_path = '/mnt/data/archive (9).zip'
gpi_csv_path = 'Global Peace Index 2023.csv'  # Extracted location inside zip

# Extracting the GPI zip file
with zipfile.ZipFile(gpi_zip_path, 'r') as zip_ref:
    zip_ref.extractall('/mnt/data/new_gpi_data')

# Loading the HDI and GDI datasets
hdi_data = pd.read_excel(hdi_file_path, skiprows=6)  
gdi_data = pd.read_excel(gdi_file_path, skiprows=6)  

# Clean HDI data
hdi_relevant = hdi_data[['Country', 'Value']].copy()  
hdi_relevant.columns = ['Country', 'HDI']

# Clean GDI data
gdi_relevant = gdi_data[['Country', 'Value']].copy()  
gdi_relevant.columns = ['Country', 'GDI']

# Load and clean GPI data
gpi_data = pd.read_csv('/mnt/data/new_gpi_data/' + gpi_csv_path)
gpi_2023 = gpi_data[gpi_data['year'] == 2023][['Country', 'Overall Scores']]
gpi_2023.columns = ['Country', 'GPI']

# Normalize GPI scores
gpi_2023['Normalized GPI'] = 1 - (gpi_2023['GPI'] - 1) / (5 - 1)

# Merging the datasets
all_data = hdi_relevant.merge(gdi_relevant, on='Country', how='inner')
all_data = all_data.merge(gpi_2023[['Country', 'Normalized GPI']], on='Country', how='inner')

# Calculate the composite index
all_data['Composite Index'] = 0.6 * all_data['HDI'] + 0.2 * all_data['GDI'] + 0.2 * all_data['Normalized GPI']

# Save the final dataset
output_file_path = '/mnt/data/Improved_HDI_Composite_Index.csv'
all_data.to_csv(output_file_path, index=False)

print("Composite Index calculation completed and saved.")
