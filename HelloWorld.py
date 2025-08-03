import sys
import os
from Utilities.ExcelData import read_excel_data

# utils_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Utilities'))
utils_path = os.environ.get('UTILITIES_PATH')
sys.path.append(utils_path)



# Load and print Excel data
data = read_excel_data()
if data is not None:
    print("📊 Excel Data:\n")
    print(data)
else:
    print("❌ Failed to load Excel data.")