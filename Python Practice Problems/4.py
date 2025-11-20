"""You are an analyst at an e-commerce company. You need to calculate the total amount a customer paid for an item by multiplying the price by the quantity."""

import pandas as pd

data = {
    'OrderID': range(1, 6),
    'UnitPrice': [10.50, 5.00, 22.00, 1.99, 15.00],
    'Quantity': [2, 5, 1, 10, 3]
}
df_orders = pd.DataFrame(data)

def calculate_total_price(df):
    df['Total_Price'] = df['UnitPrice'] * df['Quantity']
    return df
result = calculate_total_price(df_orders.copy())
print(result)