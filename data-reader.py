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
            print(soup.prettify())
    except Exception  as  e:
        print(e)