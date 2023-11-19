import glob, os, sys
from bs4 import BeautifulSoup

# Import files
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*.html")

file_contents =  glob.glob(data_path)

for file in file_contents:
    try:
        with open(file, 'r') as f:
            # Open file with Read 
            html_text = f.read()
            soup = BeautifulSoup(html_text, 'lxml')
            # print(soup.prettify())
    except Exception  as  e:
        print(e)

#####################################
# 
# Wide_attacker-provider
#
#####################################

# Find the table element
table = soup.find('table')

data_headers = []
table_headers = []
for tx in table.find_all('th'):
    table_headers.append(tx.text.strip())

data_headers.append(table_headers)

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

print(data_headers)

