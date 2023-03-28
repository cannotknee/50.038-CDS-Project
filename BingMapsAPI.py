import json
import pandas as pd

with open('test.json') as f:
    data = json.load(f)
    
target = "THE CENTRAL"
results = pd.DataFrame(data["results"])
# Find row index where searchval == The central
row = results.loc[results['SEARCHVAL'] == target].index[0]

print(results.loc[row, "LATITUDE"])