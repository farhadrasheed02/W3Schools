import pandas as pd
import os
import Module.mymodules as md
def read_excel_data():
    # Build the absolute path to the Excel file


    excel_path = os.environ.get('EXCEL_PATH')
    # excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'TestData', 'DataSheet.xlsx'))

    # Check if the file exists
    if not os.path.exists(excel_path):
        print(f"Error: The file {excel_path} does not exist.")
        return None

    # Read the Excel file
    try:
        df = pd.read_excel(excel_path)
        return df
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return None