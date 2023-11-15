import pandas as pd
import glob
import os

# Import files
imported_files = glob.glob(os.path.join('D:\web\FM-Data-Analysis-Tool\data', "*"))

if len(imported_files) > 0:
    newest_file = max(imported_files, key=os.path.getctime)
    print(newest_file)

    # Read the file
    raw_data_list = pd.read_html(newest_file, header=0, encoding="utf-8", keep_default_na=False)

    # Create a dataframe
    raw_data = raw_data_list[0]

    print(raw_data['Name'])
else:
    print("No files to process.")