import glob, os
import pandas as pd
from io import StringIO

from calculations import *

# Import files
data_path = os.path.join(os.path.join(os.path.dirname(__file__), "data"), "*.html")

file_contents = glob.glob(data_path)

# Iterate the list of file and read them
for file in file_contents:
    with open(file, "r", encoding="utf-8") as f:
        html_content = f.read()

html_content_io = StringIO(html_content)

player_data_list = pd.read_html(html_content_io, header=0)
player_data = player_data_list[0]

data_calc_values = []

calculation_functions = [
    calculate_advanced_forward_attack,
    calculate_speed_workrate_score
]

for calculation in calculation_functions:
    player_data = calculation(player_data)

# Determine earning column
earnings_columns = ["Wage", "Salary"]
valid_earnings_columns = player_data.columns[player_data.columns.isin(earnings_columns)]

# Add 'Earnings' to the DataFrame if a valid earnings column is present
if len(valid_earnings_columns) > 0:
    player_data["Wage"] = player_data[valid_earnings_columns[0]]
else:
    # If neither Wage nor Salary is present, create an 'Earnings' column with NaN values
    player_data["Wage"] = None

if "Transfer Value" not in player_data.columns:
    player_data["Transfer Value"] = None

columns_to_export = [
    "Inf",
    "Name",
    "Age",
    "Club",
    "Transfer Value",
    "Wage",
    "Nat",
    "Position",
    "Personality",
    "Media Handling",
    "Left Foot",
    "Right Foot",
    "Height",
    "Spd",
    "Jum",
    "Str",
    "Work",
] + data_calc_values

squad = player_data[columns_to_export]
print(squad)