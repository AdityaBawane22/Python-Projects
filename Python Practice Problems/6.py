"""You need to combine these two DataFrames into a single, cohesive view."""

import pandas as pd

data = {
    'TransactionID': range(201, 211),
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob', 'Eve', 'Frank', 'Alice', 'Eve'],
    'TransactionAmount': [15.50, 120.00, 45.75, 80.00, 210.50, 95.00, 15.00, 180.00, 50.00, 30.00]
}

data_loyalty = {
    'CustomerName': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'LoyaltyStatus': ['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze', 'Gold'],
    'Region': ['East', 'West', 'East', 'North', 'South', 'West', 'East']
}

df_loyalty = pd.DataFrame(data_loyalty)
df_transactions = pd.DataFrame(data)

def calculate_customer_totals(df):
    grouped = df.groupby('CustomerName')
    exp_by_cus = grouped.sum()
    return exp_by_cus
result = calculate_customer_totals(df_transactions.copy())

#print(df_loyalty)
#print(df_transactions)

def merge_customer_data(result, df_loyalty):
    merged_df = pd.merge(result, df_loyalty, on='CustomerName',how='left')
    return merged_df
final_merge = merge_customer_data(result, df_loyalty)
print(final_merge)


# result = customers are grouped by name and which customer sum of expenditure is shown
#print(result)