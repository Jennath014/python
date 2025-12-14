import pandas as pd

# Original DataFrame
df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [85, 90, 95]
})

# Row to insert
new_row = {'Name': 'X', 'Marks': 88}

# Position to insert
pos = 1  

# Insert using concat
df = pd.concat([df.iloc[:pos], pd.DataFrame([new_row]), df.iloc[pos:]]).reset_index(drop=True)

print(df)
