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
selected_headers = ["header1", "header2", "header3"]

# Loop through all files
for file in file_contents:
    try:
        with open(file, "r") as f:
            # Open file with Read
            html_text = f.read()
            soup = BeautifulSoup(html_text, "html.parser")
            # Find all table rows
            rows = soup.find_all("tr")
            # Find all headers and strip the text.
            headers = [s.text for s in rows[0].find_all("th")]
            # Print all headers
            print(headers)
            # Remove the first row (headers)
            rows = rows[1:]
            # Loop through all rows and create a dictionary
            for row in rows:
                # Finds all table data and strips the text
                row = [s.text for s in row.find_all("td")]
                output = {}
                # Loop through all headers and add to dictionary
                # Using enumerate to get the index of the header is more reliable than using the index of the row
                for idx, h in enumerate(headers):
                    # Check if the header is in the selected headers list
                    if h in selected_headers:
                        # Add the header as the key and the row data as the value
                        output[h] = row[idx]
                # Add the dictionary to the list
                dict_list.append(output)
                # Print the dictionary
            # print(json.dumps(dict_list))

            # # Write the dictionary to a json file
            # with open(f"{file}.json", "w") as f:
            #     # Write the dictionary to the file
            #     f.write(json.dumps(dict_list))

    except Exception as e:
        print(e)
