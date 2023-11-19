import glob, os
from bs4 import BeautifulSoup

# Import files
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*GKs.html")

file_contents = glob.glob(data_path)

for file in file_contents:
    try:
        with open(file, 'r') as f:
            # Open file with Read 
            data_attributes = f.read()
            soup = BeautifulSoup(data_attributes, 'lxml')
    except Exception  as  e:
        print(e)

# Find and print all table headers
headers = []
for table in soup.find_all('table'):
    headers = [th.text for th in table.find_all('th')]  

# Select certain headers
gk_essential_headers = ['Agi', 'Ref']
gk_core_headers = ['1v1', 'Ant', 'Cmd', 'Cnt', 'Kick', 'Pos']
gk_secondary_headers = ['Acc', 'Aer', 'Cmp', 'Dec', 'Fir', 'Han', 'Pas', 'Thr', 'Vis']

# Collect all the data from the table for selected headers
gk_essential_list = []
for table in soup.find_all('table'):
    for row in table.find_all('tr'):
        row_data = [td.text for td in row.find_all('td')]
        gk_essential_data = { header: value for header, value in zip(headers, row_data) if header in gk_essential_headers }
        gk_essential_list.append(gk_essential_data)
        
gk_core_list = []
for table in soup.find_all('table'):
    for row in table.find_all('tr'):
        row_data = [td.text for td in row.find_all('td')]
        gk_core_data = { header: value for header, value in zip(headers, row_data) if header in gk_core_headers }
        gk_core_list.append(gk_core_data)
        
gk_secondary_list = []
for table in soup.find_all('table'):
    for row in table.find_all('tr'):
        row_data = [td.text for td in row.find_all('td')]
        gk_secondary_data = { header: value for header, value in zip(headers, row_data) if header in gk_secondary_headers }
        gk_secondary_list.append(gk_secondary_data)
        
        print(gk_essential_list)