import pandas as pd

data = pd.read_csv('NST-EST2023-ALLDATA.csv')
filt = data[['NAME', 'POPESTIMATE2023']]
filt.to_csv('pop2023.csv', index=False)