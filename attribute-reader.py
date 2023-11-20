# Description: I want to take an HTML file that is exported from FM and turn it into a dataframe. I then want to add some columns to the dataframe and calculate some scores. I then want to export the dataframe as styled html

import pandas as pd
import glob, os

# Import the HTML file as a dataframe
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*.html")

# Get the list of files sorted by modification time
files = sorted(glob.glob(data_path), key=os.path.getmtime, reverse=True)

# Select the latest file
latest_file = files[0]

# Read the latest file as a dataframe
df = pd.read_html(latest_file)[0]
