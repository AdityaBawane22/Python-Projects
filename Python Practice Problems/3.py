"""Write a single Python function, calculate_electronics_revenue(df), that:

Filters the df_sales DataFrame to include only rows where the ProductCategory is 'Electronics'.

Calculates the sum of the Revenue column for the filtered data.

Returns the resulting total revenue as a single floating-point number."""

import pandas as pd
import numpy as np

data = {
    'OrderID': range(1001, 1011),
    'ProductCategory': ['Apparel', 'Electronics', 'Electronics', 'Home Goods', 'Apparel', 'Electronics', 'Home Goods', 'Electronics', 'Apparel', 'Apparel'],
    'Revenue': [45.50, 299.99, 150.00, 75.25, 60.00, 450.50, 12.00, 50.00, 30.00, 88.99],
    'Quantity': [1, 2, 1, 3, 1, 1, 4, 1, 2, 1]
}
df_sales = pd.DataFrame(data)

def calculate_electronics_revenue(df):
    filtered_val = df[df['ProductCategory'] == 'Electronics']

    sum_of_ele = float(filtered_val['Revenue'].sum())
    return sum_of_ele
result = calculate_electronics_revenue(df_sales)
print(result)