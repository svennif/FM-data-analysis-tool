import glob, os, sys
from bs4 import BeautifulSoup

# Read the HTML file
data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "*.html")

print(data_path)

file_contents =  glob.glob(data_path)

for file in file_contents:
    try:
        with open(file, 'r') as f:
            # Open file with Read 
            html_text = f.read()
            soup = BeautifulSoup(html_text, 'lxml')
            header_row = soup.find('tr')
            # print(header_row.prettify())
    except Exception  as  e:
        print(e)

# Find the table element
table = soup.find('table')

data_headers = []
table_headers = []
for tx in table.find_all('th'):
    table_headers.append(tx.text.strip())

data_headers.append(table_headers)
# print("\n".join(data_headers[0]))

# Find data from the following table_headers
    # Drb/90
    # Cr C/90
    # Sprints/90
    # OP-KP/90
    # xA/90

# Find the table element
table = soup.find('table')

data_headers = []
table_headers = []
for tx in table.find_all('th'):
    table_headers.append(tx.text.strip())

data_headers.append(table_headers)

# Find the index of the desired table headers
desired_headers = ['Drb/90', 'Cr C/90', 'Sprints/90', 'OP-KP/90', 'xA/90']
header_indices = [table_headers.index(header) for header in desired_headers]

# Find the data for the desired table headers
data_rows = []
for row in table.find_all('tr'):
    data_row = []
    for index in header_indices:
        data_row.append(row.find_all('td')[index].text.strip())
    data_rows.append(data_row)

# Print the data for the desired table headers
for row in data_rows:
    print(row)
