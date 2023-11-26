import glob, os, sys
from bs4 import BeautifulSoup
import json

# Import files
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*.html")

# Get all files in the data folder
file_contents = glob.glob(data_path)

# Create empty list
dict_list = []

# Define the specific headers you want to select
# Key headers will be valued 2 times higher 

mezzala_headers = ["Lon", "Tck", "Tec", "Ant", "Cmp", "Tea", "Vis", "Wor", "Acc", "Sta"]
mezzala_headers_key = ["Fir", "Pas", "Dec", "OtB"]

dm_headers = ['Mar', 'Pas', 'Agg', 'Cmp', 'Dec', 'Wor', 'Sta', 'Str']
dm_headers_key = ['Tck', 'Ant','Cnt', 'Pos', 'Tea']

bbm_headers = ['Dri', 'Fin', 'Fir', 'Lon', 'Tec', 'Agg', 'Ant', 'Cmp', 'Dec', 'Pos', 'Acc', 'Bal', 'Pac', 'Str']
bbm_headers_key = ['Pas', 'Tck', 'OtB', 'Tea', 'Wor', 'Sta']

# Loop through all files
for file in file_contents:
    try:
        with open(file, "r") as f:
            html_text = f.read()
            soup = BeautifulSoup(html_text, "html.parser")
            rows = soup.find_all("tr")
            headers = [s.text for s in rows[0].find_all("th")]
            print(headers)
            rows = rows[1:]
            for row in rows:
                row = [s.text for s in row.find_all("td")]
                output = {}
                # Loop through all headers and add to dictionary
                
            # Using enumerate to get the index of the header is more reliable than using the index of the row
            #     for idx, h in enumerate(headers):
            #         # Check if the header is in the selected headers list
            #         if h in selected_headers:
            #             # Add the header as the key and the row data as the value
            #             output[h] = row[idx]
            #     # Add the dictionary to the list
            #     dict_list.append(output)
            #     # Print the dictionary 
            # print(json.dumps(dict_list))

            # # Write the dictionary to a json file
            # with open(f"{file}.json", "w") as f:
            #     # Write the dictionary to the file
            #     f.write(json.dumps(dict_list))

    except Exception as e:
        print(e)
