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

##generating graphs and sending to the 'graphs' folder
import matplotlib.pyplot as plt
plt.figure(figsize=(12, 8))
plt.bar(products_by_volume.index, products_by_volume['Quantity'], color='#22153C')
plt.title('Ranking by Volume of Sales')
plt.xlabel('Product')
plt.ylabel('Quantity Sold')
plt.savefig('graphs/ranking_volume_sales.png')
plt.show()

##graph for revenue##
plt.figure(figsize=(12, 8))
plt.bar(products_by_revenue.index, products_by_revenue['TotalSales'], color='#11686A')
plt.title('Ranking Revenue (R$)')
plt.xlabel('Product')
plt.ylabel('Total Revenue (R$)')
plt.savefig('graphs/ranking_revenue.png')
plt.show()