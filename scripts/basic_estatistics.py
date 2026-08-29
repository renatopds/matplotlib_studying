import pandas as pd
import numpy as np
df = pd.read_csv('raw/sales_data.csv')

## information about the data
print(df.info())
## data is a str, ## we need to convert it to datetime
df['Date'] = pd.to_datetime(df['Date'])

## now, describe the data
print(df.describe())
## now, the mode of the data
print(df.mode())