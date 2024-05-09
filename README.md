# Improved-HDI-

## Overview
The `Improved_HDI.py` script is designed to compute an enhanced Human Development Index (HDI) by integrating the Gender Development Index (GDI) and the Global Peace Index (GPI). This composite index provides a more holistic view of human development by including gender equality and peace measures alongside traditional HDI metrics.

## Requirements
- Python 3.8 or higher
- Pandas library
- Numpy library
- This script assumes access to the following data files:
  - HDI data in an Excel file
  - GDI data in an Excel file
  - GPI data in a zipped CSV file

## Data Files
- **HDI Data**: `HDR23-24_Statistical_Annex_HDI_Table.xlsx`
- **GDI Data**: `HDR23-24_Statistical_Annex_GDI_Table.xlsx`
- **GPI Data**: `archive (9).zip` which contains `Global Peace Index 2023.csv`

## Setup
Ensure that Python and required libraries are installed on your machine. You can install the necessary libraries using pip:

```bash
pip install pandas numpy
```

## Running the Script
1. Place the script `Improved_HDI.py` in a directory that also contains the above-mentioned data files.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:

```bash
python Improved_HDI.py
```

## Output
The script will output a CSV file named `Improved_HDI_Composite_Index.csv`. This file contains the computed composite index for each country, combining HDI, GDI, and GPI according to predefined weights:
- HDI: 60%
- GDI: 20%
- GPI: 20%

## Notes
- Ensure all data files are in the correct format and located in the same directory as the script.
- The GPI data needs to be extracted from the zip file, which the script handles automatically.
- Modify the column names and row indices in the script if your data format differs from the expected setup.

---

