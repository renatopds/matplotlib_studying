import pandas as pd
import numpy as np
df = pd.read_csv('raw/sales_data.csv')

## information about the data
print(df.info())
## date is a str, ## we need to convert it to datetime
df['Date'] = pd.to_datetime(df['Date'])

##load trated data to a new repository ##in parquet bcs csv will format to str 
df.to_parquet('data/sales_treated.parquet')
print("Treated data saved successfully!")

## now, describe the data
print(df.describe())

## now, the mode of the data
print(df.mode())
## mean and median has the same value, so we can say that the data is symmetric


