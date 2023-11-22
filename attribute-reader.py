import glob, os, sys
from bs4 import BeautifulSoup
import json

# Import files
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*.html")

file_contents = glob.glob(data_path)

dict_list = []

for file in file_contents:
    try:
        with open(file, "r") as f:
            # Open file with Read
            html_text = f.read()
            soup = BeautifulSoup(html_text, "html.parser")
            rows = soup.find_all("tr")
            headers = [s.text for s in rows[0].find_all("th")]
            print(headers)
            rows = rows[1:]
            for row in rows:
                row = [s.text for s in row.find_all("td")]
                output = {}
                for idx, h in enumerate(headers):
                    output[h] = row[idx]
                dict_list.append(output)
            print(json.dumps(dict_list))
            with open(f"{file}.json", "w") as f:
                f.write(json.dumps(dict_list))
    except Exception as e:
        print(e)
