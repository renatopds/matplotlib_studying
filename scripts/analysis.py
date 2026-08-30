import pandas as pd
import numpy as np
df = pd.read_parquet('data/sales_treated.parquet')

## agroupying per product and summing the columns
df_grouped = df.groupby('Product')[['Quantity', 'TotalSales']].sum()

##The most and less sold products by volume
products_by_volume = df_grouped.sort_values(by='Quantity', ascending=False)
print("--- Ranking by Volume of Sales ---")
print(products_by_volume['Quantity'])

## which product brings more revenue
products_by_revenue = df_grouped.sort_values(by='TotalSales', ascending=False)
print("\n--- Ranking Revenue (R$) ---")
print(products_by_revenue['TotalSales'])