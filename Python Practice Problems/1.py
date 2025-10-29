"""Write a single Python function, `calculate_customer_metrics(df)`, that filters the sales data for non-returned items and calculates the net **TotalSpending**, 
**OrderCount**, and **AveragePurchaseValue** for each `CustomerID`."""

import pandas as pd

data = {
    'CustomerID': [101, 102, 101, 103, 102, 101, 104, 103],
    'TransactionDate': pd.to_datetime(['2023-10-01', '2023-10-05', '2023-10-06', '2023-10-08', '2023-10-10', '2023-10-15', '2023-10-18', '2023-10-20']),
    'PurchaseAmount': [50.00, 120.00, 35.50, 200.00, 75.00, 15.00, 90.00, 45.00],
    'IsReturned': [False, False, True, False, False, False, False, False]
}
df_sales = pd.DataFrame(data)
print(df_sales)

def calculate_customer_metrics(df):
    filterd_row = df_sales[df_sales['IsReturned'] == False]

    customer_summary = filterd_row.groupby('CustomerID').agg(
    Total_Purchase = ('PurchaseAmount','sum'),

    Total_orders = ('TransactionDate','count'),

    Avg_Spent_Amt = ('PurchaseAmount','mean'))

    return customer_summary
result = calculate_customer_metrics(df_sales)
print(result)